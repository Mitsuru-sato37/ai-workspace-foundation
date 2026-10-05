# Status

Status: Active cross-PC handoff entry point  
Last updated: 2026-10-05

This file is the canonical handoff document for this repository.

## Current state

- The repository is a cloud-first Python 3.12 workspace foundation.
- Python environments and dependencies are managed with `uv`; validation uses `pytest` and Ruff.
- GitHub is the source of truth for code and reproducible development state.
- Google Drive is the source of truth for durable user materials defined by the workspace architecture.
- Current active architecture and intake documents are indexed from `docs/SPEC.md`.

## Active branch

Update this field at the end of each meaningful development session.

`main`

## Completed in latest handoff

- Added a new-repository bootstrap standard and reusable templates so Work/Codex initializes future repositories with cross-PC handoff files from the start.
- Added fixed `docs/SPEC.md` and `docs/STATUS.md` entry points for cross-PC Codex recovery.
- Standardized the rule that Codex chat history is non-authoritative and handoff state must be committed and pushed.

## Next

Use `docs/12_new_repository_bootstrap.md` and `templates/repository/` whenever Work/Codex initializes a newly created repository. For ordinary work in this repository, replace this section with the concrete next task.

## Verification

Documentation-only workflow change. Verify the files exist on the pushed branch and that `AGENTS.md` points to them.

## Blockers / external dependencies

None for the handoff workflow itself.
