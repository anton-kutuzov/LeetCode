"""Shared test fixtures and helpers for LeetCode solutions.

Adds `src/main/python` to `sys.path` so test modules can import solution modules
by folder name. Folder names start with a digit, so we go through `importlib`
instead of `from ... import`:

    from tests.conftest import import_solution
    mod = import_solution("643_MaximumAverageSubarrayI")
    mod.Solution().findMaxAverage(...)
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path
from types import ModuleType

REPO_ROOT = Path(__file__).resolve().parent.parent
PY_ROOT = REPO_ROOT / "src" / "main" / "python"

if str(PY_ROOT) not in sys.path:
    sys.path.insert(0, str(PY_ROOT))


def import_solution(folder: str) -> ModuleType:
    """Import the `solution` module for a given problem folder."""
    return importlib.import_module(f"{folder}.solution")
