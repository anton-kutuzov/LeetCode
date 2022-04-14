from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        max_sum, max_sum2 = 0, 0
        prev1, prev2 = 0, 0
        for i in range(len(nums) - 1):
            f1 = nums[i + 1] + max_sum
            max_sum = max(max_sum, prev1)
            prev1 = f1
            f2 = nums[i] + max_sum2
            max_sum2 = max(max_sum2, prev2)
            prev2 = f2
        return max(max_sum, max_sum2, prev1, prev2)


solution = Solution()
print(solution.rob([1]))
print(solution.rob([2, 3, 2]))
print(solution.rob([1, 2, 3, 1]))
print(solution.rob([2, 1, 1, 2]))
print(solution.rob([1, 1]))
print(solution.rob([0]))
print(solution.rob([200, 3, 140, 20, 10]))
