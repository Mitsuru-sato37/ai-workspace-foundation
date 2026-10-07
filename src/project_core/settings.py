from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any


class SettingsError(ValueError):
    """Raised when project configuration is missing or unsafe."""


@dataclass(frozen=True)
class ProjectPaths:
    raw: Path
    processed: Path
    outputs: Path
    work: Path


@dataclass(frozen=True)
class GoogleDriveSettings:
    enabled: bool
    root_folder_name: str
    root_folder_id: str
    system_brief_id: str


@dataclass(frozen=True)
class GitHubSettings:
    enabled: bool
    repository: str


@dataclass(frozen=True)
class Settings:
    name: str
    timezone: str
    paths: ProjectPaths
    execution_mode: str
    local_required: bool
    fail_on_missing_input: bool
    write_run_manifest: bool
    google_drive: GoogleDriveSettings
    github: GitHubSettings


def _table(data: dict[str, Any], key: str) -> dict[str, Any]:
    value = data.get(key)
    if not isinstance(value, dict):
        raise SettingsError(f"[{key}] table is required")
    return value


def _text(table: dict[str, Any], key: str, *, allow_empty: bool = False) -> str:
    value = table.get(key)
    if not isinstance(value, str) or (not allow_empty and not value.strip()):
        empty_rule = "possibly empty" if allow_empty else "non-empty"
        raise SettingsError(f"{key} must be a {empty_rule} string")
    return value


def _boolean(table: dict[str, Any], key: str) -> bool:
    value = table.get(key)
    if not isinstance(value, bool):
        raise SettingsError(f"{key} must be a boolean")
    return value


def _inside(root: Path, relative: str) -> Path:
    candidate = (root / relative).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise SettingsError(f"path escapes project root: {relative}") from exc
    return candidate


def load_settings(config_path: Path, root: Path | None = None) -> Settings:
    root = (root or config_path.resolve().parents[1]).resolve()
    try:
        with config_path.open("rb") as stream:
            data = tomllib.load(stream)
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise SettingsError(f"cannot read configuration: {config_path}") from exc

    project = _table(data, "project")
    paths = _table(data, "paths")
    execution = _table(data, "execution")
    integrations = _table(data, "integrations")
    drive = _table(integrations, "google_drive")
    github = _table(integrations, "github")

    execution_mode = _text(execution, "mode")
    if execution_mode != "cloud":
        raise SettingsError("execution mode must be cloud")
    local_required = _boolean(execution, "local_required")
    if local_required:
        raise SettingsError("local_required must be false")

    drive_enabled = _boolean(drive, "enabled")

    return Settings(
        name=_text(project, "name"),
        timezone=_text(project, "timezone"),
        paths=ProjectPaths(
            raw=_inside(root, _text(paths, "raw")),
            processed=_inside(root, _text(paths, "processed")),
            outputs=_inside(root, _text(paths, "outputs")),
            work=_inside(root, _text(paths, "work")),
        ),
        execution_mode=execution_mode,
        local_required=local_required,
        fail_on_missing_input=_boolean(execution, "fail_on_missing_input"),
        write_run_manifest=_boolean(execution, "write_run_manifest"),
        google_drive=GoogleDriveSettings(
            enabled=drive_enabled,
            root_folder_name=_text(drive, "root_folder_name", allow_empty=not drive_enabled),
            root_folder_id=_text(drive, "root_folder_id", allow_empty=not drive_enabled),
            system_brief_id=_text(drive, "system_brief_id", allow_empty=not drive_enabled),
        ),
        github=GitHubSettings(
            enabled=_boolean(github, "enabled"),
            repository=_text(github, "repository", allow_empty=True),
        ),
    )
