from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from project_core.settings import SettingsError, load_settings


def config_text(raw_path: str = "data/raw", include_execution: bool = True) -> str:
    execution = """
[execution]
fail_on_missing_input = true
write_run_manifest = true
""" if include_execution else ""
    return f"""
[project]
name = "test-project"
timezone = "Asia/Tokyo"

[paths]
raw = "{raw_path}"
processed = "data/processed"
outputs = "outputs"
work = "work"
{execution}
[integrations.google_drive]
enabled = true
root_folder_name = "AI-Workspace"
root_folder_id = "folder-id"
system_brief_id = "document-id"

[integrations.github]
enabled = true
repository = ""
"""


class SettingsTests(unittest.TestCase):
    def load(self, text: str):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "config.toml"
            path.write_text(text, encoding="utf-8")
            return load_settings(path, root)

    def test_reads_expected_values(self) -> None:
        settings = self.load(config_text())
        self.assertEqual(settings.name, "test-project")
        self.assertEqual(settings.timezone, "Asia/Tokyo")
        self.assertEqual(settings.google_drive.root_folder_name, "AI-Workspace")
        self.assertTrue(settings.google_drive.enabled)
        self.assertEqual(settings.github.repository, "")

    def test_rejects_path_outside_project(self) -> None:
        with self.assertRaisesRegex(SettingsError, "escapes project root"):
            self.load(config_text("../outside"))

    def test_rejects_missing_table(self) -> None:
        with self.assertRaisesRegex(SettingsError, r"\[execution\] table is required"):
            self.load(config_text(include_execution=False))


if __name__ == "__main__":
    unittest.main()
