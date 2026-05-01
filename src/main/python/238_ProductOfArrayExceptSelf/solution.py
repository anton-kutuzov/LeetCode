from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = {}
        suffix = {}
        prefix_product = 1
        suffix_product = 1
        i = 0
        n = len(nums) - 1
        while i <= n:
            prefix[i] = prefix_product
            suffix[n - i] = suffix_product
            prefix_product *= nums[i]
            suffix_product *= nums[n - i]
            i += 1

        res = []
        i = 0
        while i <= n:
            res.append(prefix[i] * suffix[i])
            i += 1

        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert solution.productExceptSelf([-1, 1]) == [1, -1]
    assert solution.productExceptSelf([2, 2, 3]) == [6, 6, 4]
