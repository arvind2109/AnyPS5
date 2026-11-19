import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BUILD = ROOT / ".github/workflows/build.yml"
MSYS2 = ROOT / ".github/workflows/windows-msys2.yml"


def job_environment(workflow, job):
    text = workflow.read_text(encoding="utf-8")
    body = text.split(f"\n  {job}:\n", 1)[1]
    return body.split("\n    env:\n", 1)[1].split("\n    steps:\n", 1)[0]


class WindowsPythonUtf8Tests(unittest.TestCase):
    def test_windows_build_job_sets_pythonutf8(self):
        self.assertIn('PYTHONUTF8: "1"', job_environment(BUILD, "windows"))

    def test_windows_msys2_job_sets_pythonutf8(self):
        self.assertIn('PYTHONUTF8: "1"', job_environment(MSYS2, "windows-msys2"))


if __name__ == "__main__":
    unittest.main()
