"""Small shared helpers. Standard library only; no network access."""
import json
import math
import sys
from pathlib import Path


class InputError(Exception):
    pass


def project_dir(value):
    path = Path(value).expanduser().resolve(strict=True)
    if not path.is_dir():
        raise InputError("--project must point to an existing directory")
    return path


def project_path(root, value):
    if not isinstance(value, str) or not value.strip():
        raise InputError("A project-relative path must be a nonempty string")
    relative = Path(value)
    if relative.is_absolute():
        raise InputError("Use a project-relative path: " + value)
    resolved = (root / relative).resolve()
    try:
        resolved.relative_to(root)
    except ValueError:
        raise InputError("Path escapes the project directory: " + value)
    return resolved


def read_config(value):
    path = Path(value).expanduser().resolve(strict=True)
    with path.open(encoding="utf-8-sig") as handle:
        result = json.load(handle)
    if not isinstance(result, dict):
        raise InputError("Configuration must be a JSON object")
    return result


def positive_number(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise InputError(label + " must be a positive number")
    if not math.isfinite(value) or value <= 0:
        raise InputError(label + " must be a finite positive number")
    return float(value)


def emit(result, output=None):
    text = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    if output:
        path = Path(output).expanduser()
        # Exclusive creation prevents accidental replacement of earlier evidence.
        with path.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        print("Saved: " + str(path.resolve()), file=sys.stderr)
    else:
        print(text, end="")


def entrypoint(main):
    try:
        code = main()
    except (InputError, OSError, ValueError, UnicodeError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        code = 2
    raise SystemExit(0 if code is None else code)
