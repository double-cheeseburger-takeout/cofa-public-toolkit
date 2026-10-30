#!/usr/bin/env python3
"""Read a CSV and report structural quality; never modify the input."""
import argparse
import csv
import hashlib
import json
from collections import Counter
from decimal import Decimal, DecimalException, localcontext
from pathlib import Path
from _common import InputError, emit, entrypoint


def profile(path, encoding, delimiter, maximum):
    records = 0
    valid = 0
    duplicate_count = 0
    row_errors = []
    row_error_count = 0
    seen = set()
    limit_reached = False
    with path.open(encoding=encoding, newline="") as handle:
        reader = csv.reader(handle, delimiter=delimiter, strict=True)
        try:
            header = next(reader)
        except StopIteration:
            raise InputError("CSV is empty; a header row is required")
        if not header:
            raise InputError("CSV header is empty")
        stats = [{"index": i, "name": name, "blank_count": 0,
                  "numeric_count": 0, "non_numeric_count": 0,
                  "numeric_out_of_range_count": 0,
                  "_sum": Decimal(0), "_min": None, "_max": None}
                 for i, name in enumerate(header)]
        for row in reader:
            if records >= maximum:
                limit_reached = True
                break
            records += 1
            digest = hashlib.sha256(json.dumps(row, ensure_ascii=False).encode("utf-8")).digest()
            if digest in seen:
                duplicate_count += 1
            seen.add(digest)
            if len(row) != len(header):
                row_error_count += 1
                if len(row_errors) < 20:
                    row_errors.append({"record_number": records,
                                       "ending_physical_line": reader.line_num,
                                       "field_count": len(row)})
                continue
            valid += 1
            for value, item in zip(row, stats):
                value = value.strip()
                if not value:
                    item["blank_count"] += 1
                    continue
                try:
                    number = Decimal(value)
                    if not number.is_finite():
                        item["non_numeric_count"] += 1
                        continue
                except DecimalException:
                    item["non_numeric_count"] += 1
                    continue
                # Bounded precision is explicit; statistics do not infer a field's business meaning.
                try:
                    with localcontext() as context:
                        context.prec = 28
                        total = item["_sum"] + number
                except DecimalException:
                    item["numeric_out_of_range_count"] += 1
                    continue
                item["numeric_count"] += 1
                item["_sum"] = total
                item["_min"] = number if item["_min"] is None else min(item["_min"], number)
                item["_max"] = number if item["_max"] is None else max(item["_max"], number)
        for item in stats:
            count = item["numeric_count"]
            item["numeric_min"] = str(item.pop("_min")) if count else None
            item["numeric_max"] = str(item.pop("_max")) if count else None
            # Remove internal keys even when count == 0.
            item.pop("_min", None)
            item.pop("_max", None)
            total = item.pop("_sum")
            item["numeric_sum"] = str(total) if count else None
            item["numeric_mean"] = str(total / count) if count else None
    names = Counter(header)
    warnings = []
    if any(not name.strip() for name in header):
        warnings.append("blank_header")
    if any(count > 1 for count in names.values()):
        warnings.append("duplicate_header")
    if row_error_count:
        warnings.append("inconsistent_row_width")
    if limit_reached:
        warnings.append("scan_limit_reached")
    if any(item["numeric_out_of_range_count"] for item in stats):
        warnings.append("numeric_values_out_of_supported_range")
    return {"file": path.name, "encoding": encoding, "delimiter": delimiter,
            "column_count": len(header), "records_scanned": records,
            "valid_width_records": valid, "wrong_width_records": row_error_count,
            "wrong_width_examples_first_20": row_errors,
            "duplicate_record_count": duplicate_count,
            "max_rows": maximum, "scan_limit_reached": limit_reached,
            "warnings": warnings, "columns": stats,
            "notes": ["Only blank/whitespace cells count as missing. NA/null strings are not automatically converted.",
                      "Column statistics cover rows with the expected field count only.",
                      "Duplicate rows are counted but are not removed; repeated records may be legitimate.",
                      "Numeric summaries use decimal precision 28 and are strings to avoid JSON float precision loss.",
                      "Values outside the supported decimal arithmetic range are counted separately and omitted from numeric summaries.",
                      "Numeric-looking IDs are not automatically treated as measurements. Interpret the schema yourself.",
                      "No source values are changed. A quality warning is not a grading result."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file")
    parser.add_argument("--encoding", default="utf-8-sig")
    parser.add_argument("--delimiter", default=",")
    parser.add_argument("--max-rows", type=int, default=100000)
    parser.add_argument("--output", help="New JSON file; omitted means stdout")
    args = parser.parse_args()
    delimiter = "\t" if args.delimiter == "\\t" else args.delimiter
    if len(delimiter) != 1:
        raise InputError("--delimiter must be exactly one character, or \\t")
    if args.max_rows <= 0:
        raise InputError("--max-rows must be positive")
    try:
        result = profile(Path(args.file).expanduser().resolve(strict=True),
                         args.encoding, delimiter, args.max_rows)
    except csv.Error as exc:
        raise InputError("CSV parsing failed: " + str(exc))
    emit(result, args.output)
    return 1 if result["wrong_width_records"] else 0


if __name__ == "__main__":
    entrypoint(main)
