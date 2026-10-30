#!/usr/bin/env python3
"""Run explicitly configured local checks and record actual outcomes."""
import argparse
import datetime
import os
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from _common import InputError, emit, entrypoint, positive_number, project_dir, project_path, read_config


def validate(config, root):
    checks = config.get("checks")
    if not isinstance(checks, list) or not checks:
        raise InputError("checks must be a nonempty array; zero checks is not a pass")
    names = set()
    result = []
    for item in checks:
        if not isinstance(item, dict):
            raise InputError("Each check must be an object")
        name = item.get("name")
        if not isinstance(name, str) or not name.strip() or name in names:
            raise InputError("Each check needs a unique, nonempty name")
        names.add(name)
        argv = item.get("argv")
        if not isinstance(argv, list) or not argv or any(not isinstance(a, str) or not a or "\0" in a for a in argv):
            raise InputError("argv must be a nonempty array of nonempty strings")
        argv = [sys.executable if a == "{python}" else str(root) if a == "{project}" else a for a in argv]
        cwd = project_path(root, item.get("cwd", "."))
        if not cwd.is_dir():
            raise InputError("Check cwd does not exist: " + str(cwd))
        timeout = positive_number(item.get("timeout_seconds", 30), "timeout_seconds")
        result.append((name, argv, cwd, timeout))
    return result


def read_output(handle, limit):
    handle.seek(0, 2)
    size = handle.tell()
    handle.seek(0)
    if size <= limit:
        data = handle.read()
    else:
        first = handle.read(limit // 2)
        handle.seek(-(limit - limit // 2), 2)
        data = first + b"\n[... output truncated ...]\n" + handle.read()
    return data.decode("utf-8", "replace"), size > limit


def run_one(name, argv, cwd, timeout, limit):
    start = time.monotonic()
    result = {"name": name, "argv": argv, "cwd": str(cwd),
              "timeout_seconds": timeout, "returncode": None}
    with tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
        try:
            process = subprocess.Popen(argv, cwd=str(cwd), shell=False,
                                       stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                                       start_new_session=(os.name == "posix"))
            try:
                returncode = process.wait(timeout=timeout)
                result["returncode"] = returncode
                result["status"] = "passed" if returncode == 0 else "failed"
            except subprocess.TimeoutExpired:
                if os.name == "posix":
                    try:
                        os.killpg(process.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                else:
                    process.kill()
                process.wait()
                result["returncode"] = process.returncode
                result["status"] = "timed_out"
        except OSError as exc:
            result["status"] = "execution_error"
            result["error"] = str(exc)
        result["stdout"], result["stdout_truncated"] = read_output(stdout, limit)
        result["stderr"], result["stderr_truncated"] = read_output(stderr, limit)
    result["duration_seconds"] = round(time.monotonic() - start, 4)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--project", required=True)
    parser.add_argument("--output", help="New JSON file; omitted means stdout")
    parser.add_argument("--max-output-bytes", type=int, default=16000,
                        help="Retained head/tail bytes per output stream (default 16000)")
    args = parser.parse_args()
    if args.max_output_bytes < 100:
        raise InputError("--max-output-bytes must be at least 100")
    # Avoid running commands if a requested report would overwrite existing evidence.
    if args.output and os.path.lexists(os.path.expanduser(args.output)):
        raise InputError("Output already exists; choose a new report filename")
    if args.output and not Path(args.output).expanduser().parent.is_dir():
        raise InputError("The output parent directory must already exist")
    root = project_dir(args.project)
    checks = validate(read_config(args.config), root)
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    results = [run_one(*check, args.max_output_bytes) for check in checks]
    success = all(item["status"] == "passed" for item in results)
    emit({"started_at_utc": started, "project": str(root),
          "status": "passed" if success else "failed", "check_count": len(results),
          "passed_count": sum(item["status"] == "passed" for item in results),
          "checks": results,
          "note": "These are only the commands in this configuration. Passing them does not establish all requirements or predict the assessment score."}, args.output)
    return 0 if success else 1


if __name__ == "__main__":
    entrypoint(main)
