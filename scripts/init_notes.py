#!/usr/bin/env python3
"""Create one WORKLOG from the bundled blank template without overwriting."""
import argparse
from pathlib import Path
from _common import InputError, emit, entrypoint, project_dir, project_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True)
    parser.add_argument("--filename", default="WORKLOG.md",
                        help="New project-relative filename; parent must exist")
    args = parser.parse_args()
    root = project_dir(args.project)
    target = project_path(root, args.filename)
    template = Path(__file__).resolve().parent.parent / "templates" / "WORKLOG.md"
    if not template.is_file():
        raise InputError("Bundled templates/WORKLOG.md was not found")
    text = template.read_text(encoding="utf-8")
    with target.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    emit({"created": str(target), "template": "templates/WORKLOG.md",
          "note": "Fill with actual task facts. Existing files are never overwritten."})


if __name__ == "__main__":
    entrypoint(main)
