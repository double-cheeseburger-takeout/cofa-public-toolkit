"""Offline tests using only synthetic inputs and temporary directories."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


class ToolTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.project = self.base / "project"
        self.project.mkdir()

    def tearDown(self):
        self.temp.cleanup()

    def run_tool(self, name, *args):
        return subprocess.run([sys.executable, str(SCRIPTS / name)] + list(args),
                              cwd=self.base, capture_output=True, text=True,
                              encoding="utf-8", timeout=15)

    def config(self, value, name="config.json"):
        path = self.base / name
        path.write_text(json.dumps(value), encoding="utf-8")
        return str(path)

    def data(self, value, name="data.csv", encoding="utf-8"):
        path = self.project / name
        path.write_text(value, encoding=encoding)
        return str(path)

    def test_csv_bom_quotes_negative_and_missing(self):
        path = self.data('id,product,amount\n1,"A, quoted",100\n2,B,200\n3,C,-50\n4,,\n', encoding="utf-8-sig")
        result = self.run_tool("csv_profile.py", path)
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["columns"][0]["name"], "id")
        self.assertEqual(report["records_scanned"], 4)
        amount = report["columns"][2]
        self.assertEqual(amount["numeric_sum"], "250")
        self.assertEqual(amount["numeric_min"], "-50")
        self.assertEqual(amount["blank_count"], 1)
        self.assertEqual(report["columns"][1]["blank_count"], 1)

    def test_csv_ragged_rows_and_duplicate_count(self):
        path = self.data("a,b\n1,2\n1,2\n3\n")
        result = self.run_tool("csv_profile.py", path)
        self.assertEqual(result.returncode, 1)
        report = json.loads(result.stdout)
        self.assertEqual(report["duplicate_record_count"], 1)
        self.assertEqual(report["wrong_width_records"], 1)
        self.assertEqual(report["valid_width_records"], 2)

    def test_csv_limit_is_visible(self):
        path = self.data("a\n1\n2\n3\n")
        result = self.run_tool("csv_profile.py", path, "--max-rows", "2")
        self.assertEqual(result.returncode, 0)
        report = json.loads(result.stdout)
        self.assertTrue(report["scan_limit_reached"])
        self.assertEqual(report["records_scanned"], 2)

    def test_csv_out_of_range_numeric_is_reported(self):
        path = self.data("a\n1e9999999\n2\n")
        result = self.run_tool("csv_profile.py", path)
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["columns"][0]["numeric_out_of_range_count"], 1)
        self.assertEqual(report["columns"][0]["numeric_sum"], "2")
        self.assertIn("numeric_values_out_of_supported_range", report["warnings"])

    def test_csv_empty_and_bad_quoting_are_errors(self):
        empty = self.run_tool("csv_profile.py", self.data(""))
        bad = self.run_tool("csv_profile.py", self.data('a,b\n1,"unterminated\n'))
        self.assertEqual(empty.returncode, 2)
        self.assertEqual(bad.returncode, 2)

    def test_csv_existing_output_is_not_overwritten(self):
        output = self.base / "report.json"
        output.write_text("keep", encoding="utf-8")
        result = self.run_tool("csv_profile.py", self.data("a\n1\n"), "--output", str(output))
        self.assertEqual(result.returncode, 2)
        self.assertEqual(output.read_text(), "keep")

    def test_run_checks_success_failure_and_timeout(self):
        config = self.config({"checks": [
            {"name": "good", "argv": ["{python}", "-c", "print('actual pass')"]},
            {"name": "bad", "argv": ["{python}", "-c", "import sys; print('actual failure', file=sys.stderr); sys.exit(7)"]},
            {"name": "slow", "argv": ["{python}", "-c", "import time; time.sleep(5)"], "timeout_seconds": 0.1}
        ]})
        result = self.run_tool("run_checks.py", "--project", str(self.project), "--config", config)
        self.assertEqual(result.returncode, 1, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["check_count"], 3)
        self.assertEqual(report["passed_count"], 1)
        good, bad, slow = report["checks"]
        self.assertEqual(good["status"], "passed")
        self.assertIn("actual pass", good["stdout"])
        self.assertEqual(bad["returncode"], 7)
        self.assertIn("actual failure", bad["stderr"])
        self.assertEqual(slow["status"], "timed_out")

    def test_run_checks_uses_project_cwd(self):
        (self.project / "known.txt").write_text("yes")
        config = self.config({"checks": [{"name": "cwd", "argv": ["{python}", "-c", "from pathlib import Path; assert Path('known.txt').read_text() == 'yes'"]}]})
        result = self.run_tool("run_checks.py", "--project", str(self.project), "--config", config)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_zero_checks_and_string_command_are_rejected(self):
        for value in ({"checks": []}, {"checks": [{"name": "bad", "argv": "python -V"}]}):
            result = self.run_tool("run_checks.py", "--project", str(self.project), "--config", self.config(value))
            self.assertEqual(result.returncode, 2)

    def test_run_checks_invalid_executable_is_not_pass(self):
        config = self.config({"checks": [{"name": "bad", "argv": [str(self.base / "does-not-exist")]}]})
        result = self.run_tool("run_checks.py", "--project", str(self.project), "--config", config)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)["checks"][0]["status"], "execution_error")

    def test_run_checks_does_not_execute_if_report_exists(self):
        output = self.base / "report.json"
        output.write_text("keep")
        marker = self.project / "marker.txt"
        config = self.config({"checks": [{"name": "write", "argv": ["{python}", "-c", "from pathlib import Path; Path('marker.txt').write_text('bad')"]}]})
        result = self.run_tool("run_checks.py", "--project", str(self.project), "--config", config, "--output", str(output))
        self.assertEqual(result.returncode, 2)
        self.assertFalse(marker.exists())
        self.assertEqual(output.read_text(), "keep")

    def test_check_cwd_escape_rejected(self):
        config = self.config({"checks": [{"name": "escape", "cwd": "..", "argv": ["{python}", "-V"]}]})
        result = self.run_tool("run_checks.py", "--project", str(self.project), "--config", config)
        self.assertEqual(result.returncode, 2)
        self.assertIn("escapes", result.stderr)

    def test_manifest_hash_and_exclusions(self):
        (self.project / "a.txt").write_bytes(b"synthetic")
        (self.project / ".env").write_text("SECRET=synthetic-example-only")
        (self.project / ".git").mkdir()
        (self.project / ".git" / "config").write_text("internal")
        result = self.run_tool("artifact_manifest.py", "--project", str(self.project))
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["file_count"], 1)
        self.assertEqual(report["files"][0]["sha256"], hashlib.sha256(b"synthetic").hexdigest())
        self.assertNotIn("synthetic-example-only", result.stdout)

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks unavailable")
    def test_manifest_does_not_follow_symlinks(self):
        outside = self.base / "outside"
        outside.mkdir()
        (outside / "private.txt").write_text("outside")
        try:
            (self.project / "link").symlink_to(outside, target_is_directory=True)
            (self.project / "file-link").symlink_to(outside / "private.txt")
        except OSError:
            self.skipTest("platform does not permit symlink creation")
        result = self.run_tool("artifact_manifest.py", "--project", str(self.project))
        report = json.loads(result.stdout)
        self.assertEqual(report["file_count"], 0)
        self.assertEqual(len(report["skipped"]), 2)

    def test_missing_and_empty_deliverables_fail(self):
        (self.project / "empty.txt").touch()
        (self.project / "good.txt").write_text("content")
        config = self.config({"required": [{"path": "missing.txt"}, {"path": "empty.txt"}, {"path": "good.txt"}]})
        result = self.run_tool("check_deliverables.py", "--project", str(self.project), "--config", config)
        self.assertEqual(result.returncode, 1)
        checks = json.loads(result.stdout)["results"]
        self.assertEqual([item["status"] for item in checks], ["failed", "failed", "passed"])

    def test_empty_deliverable_config_and_escape_fail(self):
        for value in ({"required": []}, {"required": [{"path": "../outside.txt"}]}):
            result = self.run_tool("check_deliverables.py", "--project", str(self.project), "--config", self.config(value))
            self.assertEqual(result.returncode, 2)

    def test_init_notes_uses_own_template_and_refuses_overwrite(self):
        kit = self.base / "fake-kit"
        (kit / "scripts").mkdir(parents=True)
        (kit / "templates").mkdir()
        for name in ("init_notes.py", "_common.py"):
            shutil.copy2(SCRIPTS / name, kit / "scripts" / name)
        (kit / "templates" / "WORKLOG.md").write_text("# synthetic template\n", encoding="utf-8")
        command = [sys.executable, str(kit / "scripts" / "init_notes.py"), "--project", str(self.project)]
        first = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual((self.project / "WORKLOG.md").read_text(), "# synthetic template\n")
        second = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(second.returncode, 2)


if __name__ == "__main__":
    unittest.main()
