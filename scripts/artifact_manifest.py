#!/usr/bin/env python3
"""List local project files, byte sizes and SHA-256 hashes; no upload or archive."""
import argparse
import hashlib
import os
from pathlib import Path
from _common import emit, entrypoint, project_dir

EXCLUDED_DIRS = {".git", ".hg", ".svn", "__pycache__", "node_modules", ".venv", "venv", "env", "work-output"}


def excluded(name):
    return name == ".env" or name.startswith(".env.") or name.endswith((".pyc", ".pyo"))


def build_manifest(root, output=None):
    files = []
    skipped = []
    output_path = Path(output).expanduser().resolve() if output else None
    for directory, dirs, names in os.walk(str(root), followlinks=False):
        base = Path(directory)
        kept_dirs = []
        for name in sorted(dirs):
            path = base / name
            if path.is_symlink():
                skipped.append({"path": path.relative_to(root).as_posix(), "reason": "symlink"})
            elif name in EXCLUDED_DIRS or excluded(name):
                skipped.append({"path": path.relative_to(root).as_posix(), "reason": "excluded_directory"})
            else:
                kept_dirs.append(name)
        dirs[:] = kept_dirs
        for name in sorted(names):
            path = base / name
            relative = path.relative_to(root).as_posix()
            if path.is_symlink():
                skipped.append({"path": relative, "reason": "symlink"})
                continue
            if excluded(name) or path.resolve() == output_path:
                skipped.append({"path": relative, "reason": "excluded_file"})
                continue
            # Guard against unexpected path resolution outside the selected directory.
            path.resolve(strict=True).relative_to(root)
            if not path.is_file():
                skipped.append({"path": relative, "reason": "not_regular_file"})
                continue
            digest = hashlib.sha256()
            size = 0
            with path.open("rb") as handle:
                while True:
                    block = handle.read(1024 * 1024)
                    if not block:
                        break
                    digest.update(block)
                    size += len(block)
            files.append({"path": relative, "size_bytes": size, "sha256": digest.hexdigest()})
    files.sort(key=lambda item: item["path"])
    return {"file_count": len(files), "total_bytes": sum(item["size_bytes"] for item in files),
            "files": files, "skipped": skipped,
            "note": "Local inventory only. Default exclusions do not guarantee that other files contain no confidential information. No files were uploaded or changed."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True)
    parser.add_argument("--output", help="New JSON file; omitted means stdout")
    args = parser.parse_args()
    emit(build_manifest(project_dir(args.project), args.output), args.output)


if __name__ == "__main__":
    entrypoint(main)
