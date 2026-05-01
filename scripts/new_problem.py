"""Scaffold a new LeetCode problem (offline; no network).

Usage:
    python scripts/new_problem.py <id> <topic> <difficulty> "<Problem Title>"

Example:
    python scripts/new_problem.py 1 array easy "Two Sum"

Creates:
    src/main/python/<id>_<PascalTitle>/solution.py
    src/main/python/<id>_<PascalTitle>/README.md   # with YAML frontmatter
    tests/test_<id>_<snake_title>.py
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PY_ROOT = REPO_ROOT / "src" / "main" / "python"
TEST_ROOT = REPO_ROOT / "tests"

ALLOWED_DIFFICULTY = {"easy", "medium", "hard"}

SOLUTION_TEMPLATE = '''"""LeetCode {id}. {title}

https://leetcode.com/problems/{slug}/
"""

from __future__ import annotations


class Solution:
    def {method}(self):
        pass
'''

README_TEMPLATE = """---
id: {id}
title: {title}
slug: {slug}
difficulty: {difficulty}
topics: [{topic}]
---

# [{id}. {title}](https://leetcode.com/problems/{slug}/)

## Problem

See the [original problem on LeetCode](https://leetcode.com/problems/{slug}/).

## Approach

<!-- Describe the idea in 2-4 sentences. -->
"""

TEST_TEMPLATE = '''from tests.conftest import import_solution

mod = import_solution("{folder}")


def test_examples():
    sol = mod.Solution()
    # TODO: write parametrized cases — pick your own edge cases first.
    assert sol
'''


def to_pascal(title: str) -> str:
    parts = [w for w in title.replace("-", " ").replace("_", " ").split() if w]
    return "".join(p[0].upper() + p[1:] for p in parts)


def to_slug(title: str) -> str:
    return "-".join(w.lower() for w in title.replace("-", " ").replace("_", " ").split())


def to_snake(title: str) -> str:
    return "_".join(w.lower() for w in title.replace("-", " ").replace("_", " ").split() if w)


def to_method(title: str) -> str:
    parts = [w for w in title.replace("-", " ").replace("_", " ").split() if w]
    if not parts:
        return "solve"
    return parts[0].lower() + "".join(p[0].upper() + p[1:] for p in parts[1:])


def main(argv: list[str]) -> int:
    if len(argv) != 5:
        print(__doc__)
        return 1
    _, id_str, topic, difficulty, title = argv
    if not id_str.isdigit():
        print(f"id must be numeric, got {id_str!r}")
        return 1
    if difficulty not in ALLOWED_DIFFICULTY:
        print(f"difficulty must be one of {sorted(ALLOWED_DIFFICULTY)}, got {difficulty!r}")
        return 1

    pid = int(id_str)
    pascal = to_pascal(title)
    slug = to_slug(title)
    method = to_method(title)
    folder_name = f"{pid}_{pascal}"

    src_dir = PY_ROOT / folder_name
    if src_dir.exists():
        print(f"already exists: {src_dir}")
        return 1

    src_dir.mkdir(parents=True)
    (src_dir / "solution.py").write_text(
        SOLUTION_TEMPLATE.format(id=pid, title=title, slug=slug, method=method)
    )
    (src_dir / "README.md").write_text(
        README_TEMPLATE.format(
            id=pid, title=title, slug=slug, difficulty=difficulty, topic=topic
        )
    )

    test_path = TEST_ROOT / f"test_{pid}_{to_snake(title)}.py"
    test_path.write_text(TEST_TEMPLATE.format(folder=folder_name))

    print(f"✅ created {src_dir.relative_to(REPO_ROOT)}/")
    print(f"✅ created {test_path.relative_to(REPO_ROOT)}")
    print()
    print("Next:")
    print(f"  1. open {src_dir.relative_to(REPO_ROOT)}/solution.py and implement Solution.{method}")
    print(f"  2. add tests in {test_path.relative_to(REPO_ROOT)}")
    print("  3. run: pytest")
    print("  4. run: python scripts/generate_readme.py  # refreshes the main README")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
