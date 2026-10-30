# Status

Status: PR #7 merged
Last updated: 2026-10-30

This file is the canonical handoff document for this repository.

## Current state

- This repository provides shared development operations standards and reusable templates for repositories under `Mitsuru-sato37`.
- GitHub repositories are the source of truth for code; Google Drive is the source of truth for materials and shared documents.
- The Drive folder `AI-Workspace` contains `00_Inbox` for idea memos and `01_運用ルール` for shared operating rules.
- The foundation project's automated Drive integration remains disabled; Drive files are handled through explicit, user-authorized operations.
- Idea memos, research materials, and completed deliverables belong in Drive. GitHub holds the storage rules, procedures, and work/resumption records that link to Drive materials; the two services are not assumed to synchronize automatically.
- After each closeout PR, assess merge readiness. Ask before merging when ready; when blocked, report evidence, the exact blocker, a concrete remediation proposal, and how to verify it. Fix and recheck blockers that fall within the authorized task.
- New repository initialization uses `templates/repository/`, `scripts/initialize-repository.ps1`, and `scripts/verify-repository-bootstrap.ps1`.

## Active branch

`codex-drive-file-organization-rules`

## Completed

- Clarified the Drive/GitHub boundary: Drive holds idea memos, research materials, and completed deliverables; GitHub holds storage rules, procedures, and linked work/resumption records.
- Clarified closeout behavior: report merge readiness and ask before merging, or explain the concrete blocker and next step.
- Expanded blocked-PR guidance to include evidence, a proposed fix, and a verification step; apply in-scope fixes autonomously.

- Updated the README to match this repository's shared-foundation role, public visibility, and current GitHub / Drive boundaries.
- Added a Windows one-action initializer that copies only missing standard files by default and supports diff or explicit overwrite modes.
- Added a required-file checker that lists missing files and exits unsuccessfully.
- Added a self-test covering missing and complete repositories, exact template matches, preservation, diff, and explicit overwrite.
- Updated the bootstrap runbook and foundation instructions.
- Updated the idea-intake procedure to use `AI-Workspace/00_Inbox` and aligned the architecture and repository guidance with the current Drive source-of-truth policy.
- Added the `お疲れ` chat-closing trigger to standardize end-of-chat commit, push, and pull-request handoff with protected-branch safeguards.
- Preserved the repository-bootstrap and cross-PC handoff standards from the merged PRs.
- The first push attempt was rejected because the remote already has a `codex` branch, which conflicts with a `codex/...` ref. Renamed the local branch to `codex-drive-file-organization-rules`; no remote branch was created by the rejected attempt.
- Pushed commit `b677e9845055c7ec7c0318df8609f94a5831abc7` and opened PR #7 for review.
- PR #7 was marked ready and merged on 2026-10-24; merge commit `854a6427656d766c7de29f4f721504c047f636d1`.

## Next

- Review the GitHub/Drive connection permissions and verify each connector can access the intended repository or folder; this session's local fetch check could not write `.git/FETCH_HEAD`.
- At the end of future `お疲れ` closeouts, ask whether the user wants the conversation archived; do not archive without that explicit instruction.

## Verification

- The prior merged bootstrap PR passed its PowerShell self-test, project doctor, and Python unittest verification; this documentation-only change does not alter those code paths.
- The initial sandboxed fetch could not write `.git/FETCH_HEAD`; retrying with the required Git metadata permission succeeded. The active branch was synchronized with origin at `0/0` ahead/behind before commit.
- No tests were run for this documentation-only change. `git diff --check` passed, and a targeted consistency scan confirmed the Drive/GitHub and merge-readiness rules are present in both the active instructions and the repository template.

## Blockers / external dependencies

PR #7 is merged. This handoff update records the final state after the merge.

