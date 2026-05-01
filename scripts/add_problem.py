"""Scaffold a problem straight from a LeetCode URL.

Hits the public LeetCode GraphQL endpoint and writes:

    src/main/python/<topic>/<difficulty>/<id>_<Title>/solution.py
    src/main/python/<topic>/<difficulty>/<id>_<Title>/README.md
    tests/<topic>/<difficulty>/<id>_<Title>/test_solution.py

Then runs `scripts/generate_readme.py` to refresh the master index.

Usage:
    python scripts/add_problem.py https://leetcode.com/problems/two-sum/
    python scripts/add_problem.py two-sum
    python scripts/add_problem.py two-sum --topic hashtable
    python scripts/add_problem.py two-sum --no-tests --no-regen

Topic auto-detection picks the first matching LeetCode tag from a priority list
(see `TAG_TO_TOPIC`). Override it with `--topic`.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PY_ROOT = REPO_ROOT / "src" / "main" / "python"
TEST_ROOT = REPO_ROOT / "tests"

GRAPHQL_URL = "https://leetcode.com/graphql"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    titleSlug
    difficulty
    isPaidOnly
    topicTags { name slug }
    content
    codeSnippets { langSlug code }
  }
}
"""


def slug_from_input(arg: str) -> str:
    """Accept either a slug (`two-sum`) or a full LeetCode URL."""
    arg = arg.strip().rstrip("/")
    m = re.search(r"leetcode\.com/problems/([^/?#]+)", arg)
    if m:
        return m.group(1)
    if "/" in arg or arg.startswith("http"):
        raise SystemExit(f"could not parse LeetCode slug from: {arg}")
    return arg


def fetch_question(slug: str) -> dict:
    """POST to LeetCode's public GraphQL endpoint and return the question dict."""
    payload = json.dumps({"query": QUERY, "variables": {"titleSlug": slug}}).encode()
    req = urllib.request.Request(
        GRAPHQL_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": USER_AGENT,
            "Referer": f"https://leetcode.com/problems/{slug}/",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        raise SystemExit(f"LeetCode HTTP {e.code}: {e.reason}") from e
    if "errors" in body:
        raise SystemExit(f"LeetCode GraphQL errors: {body['errors']}")
    q = body.get("data", {}).get("question")
    if not q:
        raise SystemExit(f"no such problem: {slug}")
    return q

# First matching tag wins. Keep specific tags above general ones.
TAG_TO_TOPIC: list[tuple[str, str]] = [
    ("Linked List", "linkedlist"),
    ("Binary Search Tree", "tree"),
    ("Binary Tree", "tree"),
    ("Tree", "tree"),
    ("Stack", "stack"),
    ("Monotonic Stack", "stack"),
    ("Queue", "stack"),
    ("Monotonic Queue", "stack"),
    ("Backtracking", "backtracking"),
    ("Hash Table", "hashtable"),
    ("Two Pointers", "two_points"),
    ("Sliding Window", "two_points"),
    ("Binary Search", "binary_search"),
    ("Dynamic Programming", "dynamic_programming"),
    ("Greedy", "greedy"),
    ("String", "string"),
    ("Array", "array"),
    ("Math", "math"),
]

# -------------------- HTML → Markdown --------------------


class _HtmlToMd(HTMLParser):
    """Tiny converter targeted at LeetCode problem HTML."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self._in_pre = 0
        self._in_code = 0
        self._list_stack: list[str] = []
        self._li_index: list[int] = []

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if self._in_pre and tag in {"strong", "b", "em", "i", "code"}:
            return  # keep code blocks plain
        if tag in {"p", "div"}:
            self._ensure_blank_line()
        elif tag == "br":
            self.out.append("\n")
        elif tag == "pre":
            self._ensure_blank_line()
            self.out.append("```\n")
            self._in_pre += 1
        elif tag == "code" and not self._in_pre:
            self.out.append("`")
            self._in_code += 1
        elif tag in {"strong", "b"}:
            self.out.append("**")
        elif tag in {"em", "i"}:
            self.out.append("*")
        elif tag == "ul":
            self._ensure_blank_line()
            self._list_stack.append("ul")
        elif tag == "ol":
            self._ensure_blank_line()
            self._list_stack.append("ol")
            self._li_index.append(0)
        elif tag == "li":
            indent = "  " * max(len(self._list_stack) - 1, 0)
            if self._list_stack and self._list_stack[-1] == "ol":
                self._li_index[-1] += 1
                self.out.append(f"\n{indent}{self._li_index[-1]}. ")
            else:
                self.out.append(f"\n{indent}- ")
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self._ensure_blank_line()
            self.out.append("#" * int(tag[1]) + " ")
        elif tag == "sup":
            self.out.append("^")
        elif tag == "sub":
            self.out.append("_")

    def handle_endtag(self, tag: str) -> None:
        if self._in_pre and tag in {"strong", "b", "em", "i", "code"} and tag != "pre":
            return
        if tag in {"p", "div"}:
            self.out.append("\n\n")
        elif tag == "pre":
            self._in_pre = max(0, self._in_pre - 1)
            if not self.out[-1].endswith("\n"):
                self.out.append("\n")
            self.out.append("```\n\n")
        elif tag == "code" and self._in_code:
            self.out.append("`")
            self._in_code -= 1
        elif tag in {"strong", "b"}:
            self.out.append("**")
        elif tag in {"em", "i"}:
            self.out.append("*")
        elif tag in {"ul", "ol"}:
            if self._list_stack:
                if self._list_stack[-1] == "ol" and self._li_index:
                    self._li_index.pop()
                self._list_stack.pop()
            self.out.append("\n")
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.out.append("\n\n")

    def handle_data(self, data: str) -> None:
        self.out.append(data)

    def _ensure_blank_line(self) -> None:
        text = "".join(self.out)
        if text and not text.endswith("\n\n"):
            self.out.append("\n" if text.endswith("\n") else "\n\n")

    def render(self) -> str:
        text = "".join(self.out)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"


def html_to_md(html: str) -> str:
    parser = _HtmlToMd()
    parser.feed(html)
    return parser.render()


# -------------------- example stripping --------------------


def strip_examples_from_html(content_html: str) -> str:
    """Remove worked examples from the LeetCode HTML.

    The user wants to come up with their own test cases, so we drop:
      - every `<pre>...</pre>` block (LeetCode wraps Input/Output bodies there)
      - every `<p>` that carries an "Example N:" header
      - runs of empty `<p>&nbsp;</p>` spacers left behind
    """
    content_html = re.sub(
        r"<pre\b[^>]*>.*?</pre>", "", content_html, flags=re.DOTALL | re.IGNORECASE
    )
    content_html = re.sub(
        r"<p\b[^>]*>.*?</p>",
        lambda m: "" if re.search(r"Example\s*\d+\s*:?", m.group(0)) else m.group(0),
        content_html,
        flags=re.DOTALL | re.IGNORECASE,
    )
    content_html = re.sub(
        r"(?:<p[^>]*>\s*(?:&nbsp;|\s)*</p>\s*){2,}",
        "<p>&nbsp;</p>",
        content_html,
        flags=re.IGNORECASE,
    )
    return content_html


# -------------------- file generation --------------------


def pick_topic(tags: list[dict], override: str | None) -> str:
    if override:
        return override
    tag_names = {t["name"] for t in tags}
    for tag, topic in TAG_TO_TOPIC:
        if tag in tag_names:
            return topic
    return "math"  # fallback bucket


def pick_python_stub(snippets: list[dict]) -> str:
    by_lang = {s["langSlug"]: s["code"] for s in snippets}
    return by_lang.get("python3") or by_lang.get("python") or ""


def to_pascal(title: str) -> str:
    parts = re.findall(r"[A-Za-z0-9]+", title)
    return "".join(p[:1].upper() + p[1:] for p in parts)


def render_problem_readme(q: dict, body_md: str, primary_topic: str) -> str:
    """Per-problem README with YAML frontmatter that the index generator reads."""
    badges = {"Easy": "🟢 Easy", "Medium": "🟡 Medium", "Hard": "🔴 Hard"}
    leetcode_topics = ", ".join(t["name"] for t in q["topicTags"]) or "—"
    pid = q["questionFrontendId"]
    title = q["title"]
    slug = q["titleSlug"]
    difficulty_lower = q["difficulty"].lower()

    frontmatter = (
        "---\n"
        f"id: {pid}\n"
        f"title: {title}\n"
        f"slug: {slug}\n"
        f"difficulty: {difficulty_lower}\n"
        f"topics: [{primary_topic}]\n"
        "---\n\n"
    )
    head = (
        f"# [{pid}. {title}](https://leetcode.com/problems/{slug}/)\n\n"
        f"| Difficulty | Topics | Solution |\n"
        f"| --- | --- | --- |\n"
        f"| {badges.get(q['difficulty'], q['difficulty'])} | {leetcode_topics} | "
        f"[`solution.py`](./solution.py) |\n\n"
    )
    return (
        frontmatter
        + head
        + "## Problem\n\n"
        + body_md
        + "\n## Approach\n\n"
        + "<!-- Describe the idea in 2-4 sentences. -->\n"
    )


def render_solution_py(q: dict, stub: str) -> str:
    """Wrap the LeetCode Python3 stub with a docstring and a complete body.

    LeetCode's snippet ends after the `def ...:` line with no body, which would
    SyntaxError on import. We append `pass` (and inject typing imports for any
    type names the snippet references).
    """
    header_lines = [
        f'"""LeetCode {q["questionFrontendId"]}. {q["title"]}',
        "",
        f"https://leetcode.com/problems/{q['titleSlug']}/",
        '"""',
        "",
        "from __future__ import annotations",
    ]

    typing_names = ["List", "Optional", "Dict", "Set", "Tuple"]
    needed = [name for name in typing_names if re.search(rf"\b{name}\b", stub)]
    if needed:
        header_lines.append(f"from typing import {', '.join(needed)}")
    header_lines.extend(["", ""])

    if not stub.strip():
        stub = "class Solution:\n    def solve(self):\n        pass\n"
    else:
        # If the snippet is just a method signature with no body, append pass.
        body = stub.rstrip()
        if body.endswith(":"):
            body += "\n        pass"
        stub = body + "\n"

    return "\n".join(header_lines) + stub


def render_test_py(folder: str) -> str:
    """No example cases pre-filled — coming up with them is part of the practice."""
    return (
        "from tests.conftest import import_solution\n\n"
        f'mod = import_solution("{folder}")\n\n\n'
        "def test_examples():\n"
        "    sol = mod.Solution()\n"
        "    # TODO: write parametrized cases — pick your own edge cases first,\n"
        "    #       then add a couple from the original problem.\n"
        "    assert sol\n"
    )


def title_to_snake(title: str) -> str:
    parts = re.findall(r"[A-Za-z0-9]+", title)
    return "_".join(p.lower() for p in parts)


def write_files(q: dict, topic: str, args: argparse.Namespace) -> Path:
    pid = int(q["questionFrontendId"])
    pascal = to_pascal(q["title"])
    folder_name = f"{pid}_{pascal}"

    src_dir = PY_ROOT / folder_name
    if src_dir.exists() and not args.force:
        raise SystemExit(f"already exists: {src_dir} (use --force to overwrite)")

    src_dir.mkdir(parents=True, exist_ok=True)
    stub = pick_python_stub(q["codeSnippets"])
    (src_dir / "solution.py").write_text(render_solution_py(q, stub))

    cleaned_html = strip_examples_from_html(q["content"] or "<p>(no content)</p>")
    body_md = html_to_md(cleaned_html)
    (src_dir / "README.md").write_text(render_problem_readme(q, body_md, topic))

    if not args.no_tests:
        test_path = TEST_ROOT / f"test_{pid}_{title_to_snake(q['title'])}.py"
        if not test_path.exists() or args.force:
            test_path.write_text(render_test_py(folder_name))

    return src_dir


# -------------------- entrypoint --------------------


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("url_or_slug")
    p.add_argument("--topic", help="override auto-detected topic folder (e.g. array, stack)")
    p.add_argument("--no-tests", action="store_true", help="skip generating test file")
    p.add_argument("--no-regen", action="store_true", help="skip running generate_readme.py")
    p.add_argument("--force", action="store_true", help="overwrite existing folder")
    args = p.parse_args(argv)

    slug = slug_from_input(args.url_or_slug)
    print(f"→ fetching {slug}")
    q = fetch_question(slug)
    if q.get("isPaidOnly"):
        print(f"⚠️  '{slug}' is premium-only; content/snippets may be empty.")

    topic = pick_topic(q["topicTags"], args.topic)
    print(f"→ {q['questionFrontendId']}. {q['title']} [{q['difficulty']}] → topic={topic}")

    src_dir = write_files(q, topic, args)
    print(f"✅ wrote {src_dir.relative_to(REPO_ROOT)}/")

    if not args.no_regen:
        print("→ regenerating master README")
        subprocess.run([sys.executable, str(REPO_ROOT / "scripts/generate_readme.py")], check=True)

    print()
    print("Next:")
    print(f"  1. open {src_dir.relative_to(REPO_ROOT)}/solution.py and implement the solution")
    pid = int(q["questionFrontendId"])
    test_name = f"test_{pid}_{title_to_snake(q['title'])}.py"
    print(f"  2. flesh out the tests in tests/{test_name}")
    print("  3. run: pytest")
    return 0


if __name__ == "__main__":
    sys.exit(main())
