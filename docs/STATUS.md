# Status

Status: Active cross-PC handoff entry point  
Last updated: 2026-10-07

This file is the canonical handoff document for this repository.

## Current state

- This repository provides shared development operations standards and reusable templates for repositories under `Mitsuru-sato37`.
- GitHub repositories are the source of truth for code, specifications, and reproducible development state.
- Google Drive is a supplementary area for images, videos, Sheets, and real data that should not live in GitHub.
- New repository initialization uses `templates/repository/`, `scripts/initialize-repository.ps1`, and `scripts/verify-repository-bootstrap.ps1`.

## Active branch

`feat/repository-bootstrap-automation`

## Completed

- Updated the README to match this repository's shared-foundation role, public visibility, and current GitHub / Drive boundaries.
- Added a Windows one-action initializer that copies only missing standard files by default and supports diff or explicit overwrite modes.
- Added a required-file checker that lists missing files and exits unsuccessfully.
- Added a self-test covering missing and complete repositories, exact template matches, preservation, diff, and explicit overwrite.
- Updated the bootstrap runbook and foundation instructions.

## Next

- Review and merge the pull request.

## Verification

- `powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\test-repository-bootstrap.ps1` — PASS; covers normal and missing-file flows, all seven template hashes, and existing-file actions.
- `project doctor` — PASS in the available local clone; it still reports the deleted `AI-Workspace` folder as configured in that clone's `config/project.toml`.
- The existing Python pytest suite was not run because pytest is unavailable in the bundled Python runtime.

## Blockers / external dependencies

The existing Python test suite needs an environment with pytest installed. The legacy Drive setting is outside this bootstrap change and remains for a separate configuration review.

