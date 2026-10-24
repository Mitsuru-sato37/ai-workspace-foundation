# Status

Status: Local handoff prepared; push pending user approval
Last updated: 2026-10-24

This file is the canonical handoff document for this repository.

## Current state

- This repository provides shared development operations standards and reusable templates for repositories under `Mitsuru-sato37`.
- GitHub repositories are the source of truth for code; Google Drive is the source of truth for materials and shared documents.
- The Drive folder `AI-Workspace` contains `00_Inbox` for idea memos and `01_運用ルール` for shared operating rules.
- The foundation project's automated Drive integration remains disabled; Drive files are handled through explicit, user-authorized operations.
- New repository initialization uses `templates/repository/`, `scripts/initialize-repository.ps1`, and `scripts/verify-repository-bootstrap.ps1`.

## Active branch

`codex/drive-file-organization-rules`

## Completed

- Updated the README to match this repository's shared-foundation role, public visibility, and current GitHub / Drive boundaries.
- Added a Windows one-action initializer that copies only missing standard files by default and supports diff or explicit overwrite modes.
- Added a required-file checker that lists missing files and exits unsuccessfully.
- Added a self-test covering missing and complete repositories, exact template matches, preservation, diff, and explicit overwrite.
- Updated the bootstrap runbook and foundation instructions.
- Updated the idea-intake procedure to use `AI-Workspace/00_Inbox` and aligned the architecture and repository guidance with the current Drive source-of-truth policy.
- Added the `引き継ぎ` trigger to standardize end-of-chat commit, push, and pull-request handoff with protected-branch safeguards.
- Preserved the repository-bootstrap and cross-PC handoff standards from the merged PRs.

## Next

- When the user invokes `引き継ぎ`, push this branch and open a pull request; merge only after separate review and approval.

## Verification

- The merged bootstrap PR previously passed its PowerShell self-test, project doctor, and Python unittest verification; this documentation-only change does not alter those code paths.
- No tests were run for this documentation-only change, per user instruction. `git diff --check` is used to check patch whitespace and conflict markers.

## Blockers / external dependencies

The new branch has not been pushed. The `引き継ぎ` trigger is the user's explicit authorization for a future branch push and pull-request update.

