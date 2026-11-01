# Status

Status: idea-storage rollout complete
Last updated: 2026-11-02

This file is the canonical handoff document for this repository.

## Current state

- This repository provides shared development operations standards and reusable templates for repositories under `Mitsuru-sato37`.
- GitHub repositories are the source of truth for code; Google Drive is the source of truth for materials and shared documents.
- The Drive folder `AI-Workspace` is for cross-project shared standards and materials. `00_Inbox` holds ideas for shared rules/templates and temporarily unassigned ideas; `01_運用ルール` holds shared operating rules.
- The foundation project's automated Drive integration remains disabled; Drive files are handled through explicit, user-authorized operations.
- Project-specific idea memos belong in the relevant GitHub repository under `docs/ideas/`; cross-project ideas and temporarily unassigned ideas belong in `AI-Workspace/00_Inbox` until routed. Research materials, source data, and shared deliverables remain in Drive, with repository records linking to them.
- After each closeout PR, assess merge readiness. Ask before merging when ready; when blocked, report evidence, the exact blocker, a concrete remediation proposal, and how to verify it. Fix and recheck blockers that fall within the authorized task.
- New repository initialization uses `templates/repository/`, `scripts/initialize-repository.ps1`, and `scripts/verify-repository-bootstrap.ps1`.

## Active branch

`main` (all rollout changes and handoff updates merged)

## Current task
Completed: cross-repository idea-storage policy rollout. All seven repository PRs and the final handoff PR #12 are merged and verified; the local checkout is synchronized to `main`.

## Completed

- Merged [PR #9](https://github.com/Mitsuru-sato37/ai-workspace-foundation/pull/9) at `005c4c7400fe6731968f6626d83e8fabc034b9d9` for the Drive/GitHub storage boundary and closeout merge-readiness rules.
- Corrected this handoff record after PR #9 merged; it previously reflected the pre-merge state.
- Clarified the Drive/GitHub boundary: Drive holds idea memos, research materials, and completed deliverables; GitHub holds storage rules, procedures, and linked work/resumption records.
- Clarified closeout behavior: report merge readiness and ask before merging, or explain the concrete blocker and next step.
- Expanded blocked-PR guidance to include evidence, a proposed fix, and a verification step; apply in-scope fixes autonomously.

- Updated the README to match this repository's shared-foundation role, public visibility, and current GitHub / Drive boundaries.
- Added a Windows one-action initializer that copies only missing standard files by default and supports diff or explicit overwrite modes.
- Added a required-file checker that lists missing files and exits unsuccessfully.
- Added a self-test covering missing and complete repositories, exact template matches, preservation, diff, and explicit overwrite.
- Updated the bootstrap runbook and foundation instructions.
- At that time, set `AI-Workspace/00_Inbox` as the sole idea-memo source; the 2026-11-01 decision supersedes that scope-independent storage policy.
- Updated the foundation idea-intake procedure and architecture to store project-specific ideas in each repository and shared/unassigned ideas in `AI-Workspace`.
- Added the `お疲れ` chat-closing trigger to standardize end-of-chat commit, push, and pull-request handoff with protected-branch safeguards.
- Preserved the repository-bootstrap and cross-PC handoff standards from the merged PRs.
- The first push attempt was rejected because the remote already has a `codex` branch, which conflicts with a `codex/...` ref. Renamed the local branch to `codex-drive-file-organization-rules`; no remote branch was created by the rejected attempt.
- Pushed commit `b677e9845055c7ec7c0318df8609f94a5831abc7` and opened PR #7 for review.
- PR #7 was marked ready and merged on 2026-10-24; merge commit `854a6427656d766c7de29f4f721504c047f636d1`.

## Next
- No remaining work for this rollout.
- Future work: verify GitHub/Drive connection permissions for intended repositories and folders when needed.
- At future `お疲れ` closeouts, ask whether the user wants the conversation archived; do not archive without explicit instruction.

## Verification
- No tests were run for this documentation-only follow-up. The rollout PRs were confirmed closed and merged on their intended base branches; merge SHAs are recorded in `docs/14_shared_standard_rollout.md`.
- `meshi-roulette` had two successful `test-and-build` checks. The other six PRs had no check runs or commit statuses reported by the connected GitHub tools; branch-protection required-check settings could not be inspected.
- No submitted reviews or unresolved review threads were reported for the seven rollout PRs.
- Chuni's current public workflow files were re-read and contained none of the checked private Drive IDs/links or superseded Drive-canonical idea wording. Its existing private Drive memo remains unchanged.
- Earlier Chuni exact-text replacement attempts stopped on mismatches after branch edits had landed; the branch was inspected, repaired, and all five current Chuni files were re-read.

## Blockers / external dependencies

No blockers for the completed rollout.
