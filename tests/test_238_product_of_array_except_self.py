import pytest

from tests.conftest import import_solution

mod = import_solution("238_ProductOfArrayExceptSelf")


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
    ],
)
def test_product_except_self(nums, expected):
    assert mod.Solution().productExceptSelf(nums) == expected
