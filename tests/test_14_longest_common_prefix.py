from tests.conftest import import_solution

mod = import_solution("14_LongestCommonPrefix")


def test_examples():
    sol = mod.Solution()
    res = sol.longestCommonPrefix(["aqew", "aqety", "aqw"])
    assert res == "aq"
