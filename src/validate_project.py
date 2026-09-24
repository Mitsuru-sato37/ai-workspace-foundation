from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_DIRS = (
    "data/raw",
    "data/processed",
    "docs",
    "outputs",
    "src",
    "tests",
    "work",
)
REQUIRED_DOCS = (
    "README.md",
    "docs/README.md",
    "docs/03_runbook.md",
    "docs/10_architecture.md",
    "docs/11_idea_intake.md",
)


def validate_agents_text(text: str) -> list[str]:
    errors: list[str] = []
    marker = "# 作業規約"
    if text.count(marker) != 1:
        errors.append(f"作業規約マーカー数={text.count(marker)}（期待=1）")
        return errors

    premise, rules = text.split(marker, maxsplit=1)
    premise_lines = re.findall(r"(?m)^\d+\. ", premise)
    if not 1 <= len(premise_lines) <= 10:
        errors.append(f"プロジェクト固有前提={len(premise_lines)}行（期待=1..10）")

    headings = re.findall(r"(?m)^## (\d+)\. ", rules)
    if headings != [str(number) for number in range(1, 8)]:
        errors.append(f"規約見出し={headings!r}（期待=1..7を各1回）")
    return errors


def validate_project(root: Path) -> list[str]:
    errors: list[str] = []
    agents_path = root / "AGENTS.md"
    if not agents_path.is_file():
        errors.append("AGENTS.mdがない")
    else:
        errors.extend(validate_agents_text(agents_path.read_text(encoding="utf-8")))

    for relative in REQUIRED_DIRS:
        if not (root / relative).is_dir():
            errors.append(f"ディレクトリがない: {relative}")
    for relative in REQUIRED_DOCS:
        path = root / relative
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"文書がないか空: {relative}")
    return errors


def self_test() -> None:
    malformed = "# プロジェクト固有の前提（仮置き）\n1. 仮\n# 作業規約\n## 1. 返し方\n"
    errors = validate_agents_text(malformed)
    if not errors:
        raise AssertionError("壊れた規約（2〜7欠落）を検出できなかった")
    print(f"SELF-TEST OK: 壊れた規約を{len(errors)}件のエラーとして検出")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    if args.self_test:
        self_test()

    errors = validate_project(args.root)
    checked = 1 + len(REQUIRED_DIRS) + len(REQUIRED_DOCS)
    if errors:
        for error in errors:
            print(f"NG: {error}")
        return 1
    print(
        f"OK: {checked}対象を検査"
        f"（AGENTS.md 1、ディレクトリ {len(REQUIRED_DIRS)}、文書 {len(REQUIRED_DOCS)}）"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
