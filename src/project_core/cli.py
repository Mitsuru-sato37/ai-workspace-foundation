from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from pathlib import Path

from project_core.settings import SettingsError, load_settings


def doctor(root: Path) -> int:
    try:
        settings = load_settings(root / "config" / "project.toml", root)
    except SettingsError as exc:
        print(json.dumps({"status": "ng", "error": str(exc)}, ensure_ascii=False))
        return 1

    paths = {
        "raw": settings.paths.raw,
        "processed": settings.paths.processed,
        "outputs": settings.paths.outputs,
        "work": settings.paths.work,
    }
    missing = [name for name, path in paths.items() if not path.is_dir()]
    payload = {
        "status": "ok" if not missing else "ng",
        "project": settings.name,
        "timezone": settings.timezone,
        "execution_mode": settings.execution_mode,
        "local_required": settings.local_required,
        "paths_checked": len(paths),
        "missing_paths": missing,
        "google_drive": {
            "enabled": settings.google_drive.enabled,
            "root_folder_name": settings.google_drive.root_folder_name,
            "configured": bool(settings.google_drive.root_folder_id),
        },
        "github": {
            "enabled": settings.github.enabled,
            "configured": bool(settings.github.repository),
        },
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if not missing else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="project")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("doctor", help="設定と必須ディレクトリを検査する")
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parents[2]
    if args.command == "doctor":
        return doctor(root)
    return 2
