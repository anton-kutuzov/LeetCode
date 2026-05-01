import pytest

from tests.conftest import import_solution

mod = import_solution("53_MaximumSubarray")


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1], -1),
        ([-2, -1], -1),
    ],
)
def test_max_subarray(nums, expected):
    assert mod.Solution().maxSubArray(nums) == expected
