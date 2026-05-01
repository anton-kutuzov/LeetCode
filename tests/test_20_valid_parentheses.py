import pytest

from tests.conftest import import_solution

mod = import_solution("20_ValidParentheses")


@pytest.mark.parametrize(
    "s,expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
    ],
)
def test_is_valid(s, expected):
    assert mod.Solution().isValid(s) is expected
