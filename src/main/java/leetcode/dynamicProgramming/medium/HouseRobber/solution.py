from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        f = [0 for _ in nums]
        max_sum = 0
        for i in range(len(nums)):
            f[i] = nums[i] + max_sum
            max_sum = max(max_sum, f[i-1])
        return max(f)


solution = Solution()
print(solution.rob([1, 2, 3, 1]))
print(solution.rob([2, 7, 9, 3, 1]))
print(solution.rob([2, 1, 1, 2]))
print(solution.rob([1, 1]))
print(solution.rob([1]))
print(solution.rob([0]))
print(solution.rob([]))
