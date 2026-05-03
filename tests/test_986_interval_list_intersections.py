from tests.conftest import import_solution

mod = import_solution("986_IntervalListIntersections")


def test_examples():
    sol = mod.Solution()
    first_list = [[1, 4], [6, 8], [9, 12]]
    second_list = [[2, 9], [12, 13]]
    res = sol.intervalIntersection(first_list, second_list)
    assert res == [[2, 4], [6, 8], [9, 9], [12, 12]]
