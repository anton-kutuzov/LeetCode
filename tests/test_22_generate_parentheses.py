import pytest

from tests.conftest import import_solution

mod = import_solution("22_GenerateParentheses")


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    ],
)
def test_generate_parenthesis(n, expected):
    assert sorted(mod.Solution().generateParenthesis(n)) == sorted(expected)
