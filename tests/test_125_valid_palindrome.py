import pytest

from tests.conftest import import_solution

mod = import_solution("125_ValidPalindrome")


@pytest.mark.parametrize(
    "s,expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
        ("ab_a", True),
    ],
)
def test_is_palindrome(s, expected):
    assert mod.Solution().isPalindrome(s) is expected
