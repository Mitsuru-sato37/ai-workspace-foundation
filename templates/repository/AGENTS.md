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

## Project-specific rules

Replace this section with the project's actual implementation, product, security, and verification rules. Do not leave generic placeholders once implementation begins.
