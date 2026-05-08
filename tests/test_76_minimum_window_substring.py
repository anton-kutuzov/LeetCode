from tests.conftest import import_solution

mod = import_solution("76_MinimumWindowSubstring")


def test_examples():
    sol = mod.Solution()
    res = sol.minWindow("ADOBECODEBANC", "ABC")
    assert res == "BANC"


def test_examples_with_only_one_element():
    sol = mod.Solution()
    res = sol.minWindow("a", "b")
    assert res == ""


def test_examples_with_equal_elements():
    sol = mod.Solution()
    res = sol.minWindow("aa", "aa")
    assert res == "aa"
