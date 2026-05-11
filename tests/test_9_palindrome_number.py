from tests.conftest import import_solution

mod = import_solution("9_PalindromeNumber")


def test_examples():
    sol = mod.Solution()
    assert not sol.isPalindrome(123)
    assert sol.isPalindrome(121)
    assert not sol.isPalindrome(-121)
    assert not sol.isPalindrome(123123)
