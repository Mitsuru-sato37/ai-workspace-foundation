# Project instructions

## Source of truth

Before making changes, read in this order:

1. `README.md` when present
2. `docs/SPEC.md`
3. `docs/STATUS.md`
4. project-specific canonical documents referenced by those files

Do not treat Codex chat history as a source of truth. Durable requirements, decisions, status, and next steps belong in this repository.

## Cross-PC workflow

GitHub is the shared source of truth across PCs.

At the start of work:

```bash
git status
git fetch origin
```

Preserve unrelated local changes. Read `docs/STATUS.md`, switch to the recorded active branch when appropriate, and pull with `git pull --ff-only`.

For a new coherent task, use a dedicated branch when appropriate.

Before handing work to another PC:

1. update the canonical handoff referenced by `docs/STATUS.md`;
2. record active branch, completed work, next work, verification, and blockers;
3. commit intended changes;
4. push the active branch;
5. confirm GitHub contains the handoff update.

Never leave the only copy of important work in uncommitted local files, terminal output, or a Codex conversation.

## Comprehensive debugging

When the user asks for a comprehensive debug pass, an overall debug, or equivalent app-wide verification:

1. read `docs/DEBUG_STANDARD.md` and `docs/DEBUG_MATRIX.md` after the specification sources;
2. establish the current baseline by running the real project verification commands;
3. expand `docs/DEBUG_MATRIX.md` with missing project-specific normal, error, boundary, state-transition, persistence, external-dependency, and UI cases;
4. for reproducible bugs, add a regression test where practical and confirm it fails before the fix;
5. apply the smallest fix that preserves the specification;
6. rerun the targeted test, full tests, static checks, and production build as applicable;
7. update `docs/DEBUG_MATRIX.md` and `docs/STATUS.md`;
8. commit and push the work so the debug result is recoverable from GitHub.

Do not call the comprehensive debug complete while a known Critical or High severity bug remains unresolved. Report the result under: PASS / fixed bugs / unverified items / external dependencies.

## Project-specific rules

Replace this section with the project's actual implementation, product, security, and verification rules. Do not leave generic placeholders once implementation begins.


## Quick Git sync check

On Windows, run this from the repository root at the start of work and before handing work to another PC:

```powershell
.\git-status.cmd
```

It fetches `origin` and reports the current branch, uncommitted changes, whether pull or push is needed, and whether the current feature branch is merged into `main`. If GitHub CLI (`gh`) is available, PR state is used for a more precise merge result; otherwise Git history/patch equivalence is used as a fallback.
