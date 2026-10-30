#!/usr/bin/env python3
"""Report local tool versions without reading credentials or installing anything."""
import argparse
import platform
import shutil
import subprocess
import sys
from _common import emit, entrypoint


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", help="New JSON file; omitted means stdout")
    args = parser.parse_args()
    tools = []
    for name in ("git", "node", "npm"):
        location = shutil.which(name)
        item = {"name": name, "available": bool(location)}
        if location:
            try:
                result = subprocess.run([location, "--version"], capture_output=True,
                                        text=True, errors="replace", timeout=5,
                                        shell=False)
                item.update(returncode=result.returncode,
                            version=(result.stdout or result.stderr).strip()[:500])
            except (OSError, subprocess.TimeoutExpired) as exc:
                item["error"] = type(exc).__name__
        tools.append(item)
    emit({"system": platform.system(), "release": platform.release(),
          "machine": platform.machine(), "python": platform.python_version(),
          "python_implementation": platform.python_implementation(),
          "python_executable": sys.executable, "tools": tools,
          "note": "Version inventory only. Missing tools are not installed. Environment variables and credential files are not read."},
         args.output)


if __name__ == "__main__":
    entrypoint(main)
