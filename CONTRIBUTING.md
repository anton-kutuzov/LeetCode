# Contributing

This is a personal practice repo, but it's set up so that adding a new problem is mechanical.

## Add a new problem

### Preferred: from a LeetCode URL

```bash
python scripts/add_problem.py https://leetcode.com/problems/two-sum/
```

Hits the LeetCode GraphQL API and writes:

- `src/main/python/<id>_<Title>/solution.py` — pre-filled with the LeetCode
  Python signature, `pass` body, and the right `typing` imports
- `src/main/python/<id>_<Title>/README.md` — YAML frontmatter
  (`id`, `title`, `slug`, `difficulty`, `topics`) + problem statement +
  approach placeholder
- `tests/test_<id>_<snake_title>.py` — empty test stub

The primary topic comes from the LeetCode tags (priority list in
`scripts/add_problem.py`); override with `--topic stack`.

```bash
python scripts/add_problem.py <url> --topic stack       # override topic
python scripts/add_problem.py <url> --no-tests          # skip test scaffold
python scripts/add_problem.py <url> --no-regen          # skip README regen
python scripts/add_problem.py <url> --force             # overwrite
```

### Manual: when the network is offline

```bash
python scripts/new_problem.py 1 array easy "Two Sum"
```

## Repository layout

```
src/main/python/<id>_<PascalCaseTitle>/
    solution.py        # LeetCode Solution class
    README.md          # YAML frontmatter + problem statement + approach
tests/test_<id>_<snake_title>.py
```

The flat structure means each problem lives in exactly one place; topic and
difficulty are tags in the README frontmatter. A problem can list multiple
topics — `topics: [array, two_points]` — and it'll appear under both sections
in the master index.

## Why frontmatter?

Folder hierarchies like `topic/difficulty/problem/` lock each problem into a
single category, which is wrong about half the time (LRU Cache is hash-table
*and* linked-list; Maximum Subarray is array *and* DP). YAML tags fix this
without any folder reshuffling — the master README groups by tag.

The format:

```yaml
---
id: 643
title: Maximum Average Subarray I
slug: maximum-average-subarray-i
difficulty: easy
topics: [array, two_points]   # primary first; can have multiple
---
```

## Running checks locally

```bash
pip install -e '.[dev]'
pre-commit install   # optional but recommended

pytest               # tests
ruff check .         # lint
ruff format .        # format
```

## After scaffolding

1. implement `Solution` in `solution.py`
2. write real cases in `tests/test_<id>_<title>.py`
3. run `pytest`
4. (only needed for manual scaffolding) `python scripts/generate_readme.py`
