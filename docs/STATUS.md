# Status

Status: PR #9 merged
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

`codex-pr9-status-correction` (follow-up handoff correction for merged PR #9)

## Current task

Active task: propagate the idea-storage policy across the repository template and all six other accessible repositories. Seven PRs are open; merge and verify all applicable PRs before marking the rollout complete.

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

- Review the GitHub/Drive connection permissions and verify each connector can access the intended repository or folder; this session's local fetch check could not write `.git/FETCH_HEAD`.
- At the end of future `お疲れ` closeouts, ask whether the user wants the conversation archived; do not archive without that explicit instruction.
- Check required-check rules for all seven PR base branches; refresh the PR diagnostics. Once required checks are verified, obtain merge authorization, merge foundation first, then the six project PRs, and confirm each intended branch update.

## Verification

- The prior merged bootstrap PR passed its PowerShell self-test, project doctor, and Python unittest verification; this documentation-only change does not alter those code paths.
- The initial sandboxed fetch could not write `.git/FETCH_HEAD`; retrying with the required Git metadata permission succeeded. The active branch was synchronized with origin at `0/0` ahead/behind before commit.
- No tests were run for this documentation-only change. `git diff --check` passed, and a targeted consistency scan confirmed the Drive/GitHub and merge-readiness rules are present in both the active instructions and the repository template.
- PR #9 targeted `main`; GitHub showed no conflicts and enabled the merge action. Although connected-tool check diagnostics returned zero check runs and zero commit statuses, GitHub accepted the merge, which was confirmed at `005c4c7400fe6731968f6626d83e8fabc034b9d9`.
- This task: GitHub listed seven non-archived repositories under the account (foundation plus six projects); visibility and each applicable AGENTS/STATUS were checked. Seven PRs are open and tracked in `docs/14_shared_standard_rollout.md`. The Chuni project has one pre-existing private Drive candidate memo; its source was read, kept unchanged, and excluded from public file details. Five project PRs update AGENTS and STATUS; Chuni's PR also changes its project-specific candidate workflow and removes private Drive pointers. No tests were run for these documentation-only changes. `git diff --check` passed. Foundation changes and this handoff are pushed to the active branch `codex-pr9-status-correction`; its GitHub head includes the latest handoff update.
- PR readiness: all seven target branches match the intended base and currently report mergeable with no review submissions or unresolved review threads. `meshi-roulette` has two successful checks; the other six PRs have no check runs or statuses. Branch protection / required-check rules could not be verified with the connected tools, so merge readiness remains unverified.

## Blockers / external dependencies

PR #9 is merged. The foundation PR #11 and six project PRs are open; cross-repository propagation remains incomplete until each applicable PR is merged. Required-check settings for the seven base branches also need verification before merge.

