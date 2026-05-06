"""LeetCode 15. 3Sum

https://leetcode.com/problems/3sum/
"""

from __future__ import annotations


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        answer = []
        nums = sorted(nums)
        l = len(nums) - 1
        for n in range(l - 1):

            if n > 0 and nums[n] == nums[n - 1]:
                continue

            i = n + 1
            j = l

            while i < j:
                if j < l and nums[j] == nums[j + 1]:
                    j -= 1
                    continue
                if i > n + 1 and nums[i] == nums[i - 1]:
                    i += 1
                    continue
                if nums[i] + nums[j] + nums[n] == 0:
                    answer.append([nums[i], nums[j], nums[n]])
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] + nums[n] > 0:
                    j -= 1
                elif nums[i] + nums[j] + nums[n] < 0:
                    i += 1

        return answer
