# Status

Status: Active cross-PC handoff entry point  
Last updated: 2026-10-07

This file is the canonical handoff document for this repository.

## Current state

- This repository provides shared development operations standards and reusable templates for repositories under `Mitsuru-sato37`.
- GitHub repositories are the source of truth for code, specifications, and reproducible development state.
- Google Drive is a supplementary area for images, videos, Sheets, and real data that should not live in GitHub. The root `Tottoko` spreadsheet is the idea ledger; it is not a folder for project files.
- The foundation project's Google Drive integration is disabled until a current project Drive folder is configured.
- New repository initialization uses `templates/repository/`, `scripts/initialize-repository.ps1`, and `scripts/verify-repository-bootstrap.ps1`.

## Active branch

`feat/repository-bootstrap-automation`

## Completed

- Updated the README to match this repository's shared-foundation role, public visibility, and current GitHub / Drive boundaries.
- Added a Windows one-action initializer that copies only missing standard files by default and supports diff or explicit overwrite modes.
- Added a required-file checker that lists missing files and exits unsuccessfully.
- Added a self-test covering missing and complete repositories, exact template matches, preservation, diff, and explicit overwrite.
- Updated the bootstrap runbook and foundation instructions.
- Disabled the obsolete project-level Drive integration and cleared its deleted folder/document IDs; aligned the current idea-intake guide with the `Tottoko` spreadsheet.

## Next

- Review and merge the pull request.

## Verification

- `powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\test-repository-bootstrap.ps1` — PASS; covers normal and missing-file flows, all seven template hashes, and existing-file actions.
- `project doctor` — PASS; the Google Drive integration is disabled and reports no configured folder reference.
- `python -m unittest discover -s tests` — PASS; six settings tests cover enabled and disabled Drive configuration.
- The pytest runner is unavailable in the bundled Python runtime; the existing test cases were run with Python unittest.

## Blockers / external dependencies

The pytest runner is unavailable in the bundled Python runtime. The Python unit tests passed through unittest discovery.

