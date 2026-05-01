"""Regenerate the top-level README and per-problem READMEs from the filesystem.

The repo layout is the canonical source of truth: each solved problem lives at
`src/main/python/<id>_<PascalCaseTitle>/solution.py`. Topic and difficulty
metadata live in YAML frontmatter at the top of each per-problem `README.md`,
so a single problem can appear under multiple topic groups in the master index.

Run from repo root:
    python scripts/generate_readme.py
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PY_ROOT = REPO_ROOT / "src" / "main" / "python"

# Display ordering / labels for known topics.
TOPIC_ORDER = [
    "array",
    "string",
    "linkedlist",
    "tree",
    "stack",
    "hashtable",
    "two_points",
    "binary_search",
    "dynamic_programming",
    "greedy",
    "backtracking",
    "math",
]
TOPIC_LABELS = {
    "array": "Array",
    "string": "String",
    "linkedlist": "Linked List",
    "tree": "Tree",
    "stack": "Stack",
    "hashtable": "Hash Table",
    "two_points": "Two Pointers",
    "binary_search": "Binary Search",
    "dynamic_programming": "Dynamic Programming",
    "greedy": "Greedy",
    "backtracking": "Backtracking",
    "math": "Math",
}

DIFFICULTY_ORDER = ["easy", "medium", "hard"]
DIFFICULTY_BADGES = {
    "easy": "🟢 Easy",
    "medium": "🟡 Medium",
    "hard": "🔴 Hard",
}


@dataclass
class Problem:
    id: int
    title: str
    slug: str
    difficulty: str
    topics: list[str]
    folder: Path

    @property
    def folder_rel(self) -> str:
        return self.folder.relative_to(REPO_ROOT).as_posix()

    @property
    def url(self) -> str:
        return f"https://leetcode.com/problems/{self.slug}/"


def parse_frontmatter(text: str) -> dict[str, object]:
    """Tiny YAML-ish frontmatter parser. Supports `key: value` and `key: [a, b]`."""
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    block = text[4:end]
    out: dict[str, object] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            out[key] = [s.strip() for s in inner.split(",") if s.strip()] if inner else []
        elif value.isdigit():
            out[key] = int(value)
        else:
            out[key] = value
    return out


def discover_problems() -> list[Problem]:
    problems: list[Problem] = []
    for solution in PY_ROOT.rglob("solution.py"):
        folder = solution.parent
        m = re.match(r"^(\d+)_(.+)$", folder.name)
        if not m:
            continue
        readme = folder / "README.md"
        if not readme.exists():
            print(f"⚠️  {folder.name}: README.md missing — skip")
            continue
        meta = parse_frontmatter(readme.read_text())
        if not meta:
            print(f"⚠️  {folder.name}: README.md has no frontmatter — skip")
            continue
        problems.append(
            Problem(
                id=int(meta.get("id", m.group(1))),
                title=str(meta.get("title", m.group(2))),
                slug=str(meta.get("slug", "")),
                difficulty=str(meta.get("difficulty", "medium")),
                topics=list(meta.get("topics", [])),
                folder=folder,
            )
        )
    problems.sort(key=lambda p: p.id)
    return problems


def render_main_readme(problems: list[Problem]) -> str:
    by_difficulty = Counter(p.difficulty for p in problems)
    by_topic: dict[str, list[Problem]] = defaultdict(list)
    for p in problems:
        for t in p.topics or ["math"]:
            by_topic[t].append(p)
    for plist in by_topic.values():
        plist.sort(
            key=lambda p: (
                DIFFICULTY_ORDER.index(p.difficulty)
                if p.difficulty in DIFFICULTY_ORDER
                else 99,
                p.id,
            )
        )

    total = len(problems)
    easy = by_difficulty.get("easy", 0)
    medium = by_difficulty.get("medium", 0)
    hard = by_difficulty.get("hard", 0)

    def badge(label: str, value: object, color: str) -> str:
        safe = label.replace(" ", "%20")
        return f"![{label}](https://img.shields.io/badge/{safe}-{value}-{color})"

    header = f"""# LeetCode

My LeetCode practice in Python. Started this repo back in 2020 in Java, rebooted
it in Python in 2025 — the old Java solutions are still under `src/main/java/`
if anyone's curious.

Each problem lives in its own folder under `src/main/python/`: the solution, a
short README with the link and a couple notes about how I thought about it, and
pytest tests for the ones I've cleaned up. Whenever I notice a pattern repeats
across problems I jot it down in [docs/PATTERNS.md](docs/PATTERNS.md) — that's
turned into a decent "what shape is this problem" cheatsheet for myself.

{badge("Solved", total, "blue")} {badge("Easy", easy, "brightgreen")} {badge("Medium", medium, "yellow")} {badge("Hard", hard, "red")}

| Total | Easy | Medium | Hard |
| :---: | :---: | :---: | :---: |
| **{total}** | {easy} | {medium} | {hard} |

## Solutions
"""

    sections: list[str] = [header]
    seen_topics = set()
    for topic in [*TOPIC_ORDER, *sorted(t for t in by_topic if t not in TOPIC_ORDER)]:
        if topic not in by_topic or topic in seen_topics:
            continue
        seen_topics.add(topic)
        plist = by_topic[topic]
        sections.append(f"\n### {TOPIC_LABELS.get(topic, topic.replace('_', ' ').title())} ({len(plist)})\n")
        sections.append("| # | Title | Difficulty | Solution |")
        sections.append("| ---: | --- | :---: | :---: |")
        for p in plist:
            badge_label = DIFFICULTY_BADGES.get(p.difficulty, p.difficulty)
            sections.append(
                f"| {p.id} | [{p.title}]({p.url}) | {badge_label} "
                f"| [📁]({p.folder_rel}) |"
            )

    return "\n".join(sections) + "\n"


def write_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text() == content:
        return False
    path.write_text(content)
    return True


def main() -> None:
    problems = discover_problems()
    print(f"discovered {len(problems)} problems")

    main_readme = REPO_ROOT / "README.md"
    if write_if_changed(main_readme, render_main_readme(problems)):
        print(f"updated {main_readme.relative_to(REPO_ROOT)}")
    else:
        print("main README unchanged")


if __name__ == "__main__":
    main()
