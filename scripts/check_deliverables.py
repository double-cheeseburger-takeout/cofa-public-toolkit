#!/usr/bin/env python3
"""Check explicitly listed local deliverable paths, not their functional quality."""
import argparse
from _common import InputError, emit, entrypoint, project_dir, project_path, read_config


def inspect(config, root):
    required = config.get("required")
    if not isinstance(required, list) or not required:
        raise InputError("required must be a nonempty array")
    results = []
    seen = set()
    for item in required:
        if not isinstance(item, dict):
            raise InputError("Each required entry must be an object")
        raw = item.get("path")
        path = project_path(root, raw)
        if raw in seen:
            raise InputError("Duplicate required path: " + raw)
        seen.add(raw)
        kind = item.get("kind", "file")
        if kind not in ("file", "directory"):
            raise InputError("kind must be file or directory")
        nonempty = item.get("nonempty", True)
        if not isinstance(nonempty, bool):
            raise InputError("nonempty must be a JSON boolean")
        reason = None
        if not path.exists():
            reason = "missing"
        elif kind == "file" and not path.is_file():
            reason = "not_a_file"
        elif kind == "directory" and not path.is_dir():
            reason = "not_a_directory"
        elif nonempty and kind == "file" and path.stat().st_size == 0:
            reason = "empty_file"
        elif nonempty and kind == "directory" and next(path.iterdir(), None) is None:
            reason = "empty_directory"
        result = {"path": raw, "kind": kind, "status": "failed" if reason else "passed"}
        if reason:
            result["reason"] = reason
        results.append(result)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True)
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", help="New JSON file; omitted means stdout")
    args = parser.parse_args()
    results = inspect(read_config(args.config), project_dir(args.project))
    success = all(item["status"] == "passed" for item in results)
    emit({"status": "passed" if success else "failed", "required_count": len(results),
          "results": results,
          "note": "Presence/type/nonempty checks only. This does not validate answers, task requirements, hidden tests, or actual submission receipt."}, args.output)
    return 0 if success else 1


if __name__ == "__main__":
    entrypoint(main)
