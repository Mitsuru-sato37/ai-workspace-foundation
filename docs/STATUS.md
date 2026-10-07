# Status

Status: Active cross-PC handoff entry point  
Last updated: 2026-10-07

This file is the canonical handoff document for this repository.

## Current state

- The repository is a cloud-first Python 3.12 workspace foundation.
- Python environments and dependencies are managed with `uv`; validation uses `pytest` and Ruff.
- GitHub is the source of truth for code and reproducible development state.
- Google Drive is the source of truth for durable user materials defined by the workspace architecture.
- Current active architecture and intake documents are indexed from `docs/SPEC.md`.

## Active branch

Update this field at the end of each meaningful development session.

`debug-standard-template-2026-10-07`

## Completed in latest handoff

- Added reusable `docs/DEBUG_STANDARD.md` and `docs/DEBUG_MATRIX.md` templates for all future application repositories.
- Added `docs/13_debugging_workflow.md` so a short request such as 「総合デバッグして」 maps to the same specification-first debug workflow.
- Updated the repository template `AGENTS.md` so Codex performs baseline verification, scenario expansion, regression-test-first bug fixes, full re-verification, documentation, and GitHub handoff automatically.
- Updated the new-repository bootstrap standard so debug standard/matrix files are required from repository initialization.

## Next

Merge this standardization change. After that, every newly initialized application repository should start with the debug standard and matrix. Existing repositories without them should adopt the templates at the start of their next comprehensive debug pass.

## Verification

Documentation/template-only workflow change. Verify the two debug template files and `docs/13_debugging_workflow.md` exist on the pushed branch, and verify both foundation/bootstrap instructions and repository-template `AGENTS.md` reference the debug workflow.

## Blockers / external dependencies

None for the handoff workflow itself.
