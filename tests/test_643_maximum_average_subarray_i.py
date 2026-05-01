import pytest

from tests.conftest import import_solution

mod = import_solution("643_MaximumAverageSubarrayI")


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 12, -5, -6, 50, 3], 4, 12.75),
        ([5], 1, 5.0),
        ([0, 4, 0, 3, 2], 1, 4.0),
        ([-1, -2, -3, -4], 2, -1.5),
    ],
)
def test_find_max_average(nums, k, expected):
    assert mod.Solution().findMaxAverage(nums, k) == pytest.approx(expected)
