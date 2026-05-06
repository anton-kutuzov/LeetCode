from tests.conftest import import_solution

mod = import_solution("15_3Sum")


def test_examples():
    sol = mod.Solution()
    result = sol.threeSum([-1, 0, 1, 2, -1, -4])
    assert len(result) == 2
    for res in result:
        assert sorted(res) in [[-1, -1, 2], [-1, 0, 1]]


def test_examples_with_zeros():
    sol = mod.Solution()
    result = sol.threeSum([0, 0, 0])
    assert len(result) == 1
    for res in result:
        assert sorted(res) in [[0, 0, 0]]


def test_examples_with_double_zeros_answer():
    sol = mod.Solution()
    result = sol.threeSum([1, 2, 0, 1, 0, 0, 0, 0])
    assert len(result) == 1
    for res in result:
        assert sorted(res) in [[0, 0, 0]]
