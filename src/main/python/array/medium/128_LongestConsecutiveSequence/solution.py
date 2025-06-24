from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length = 0

        for n in nums:
            i = 0
            while n + i in nums_set:
                i += 1
            length = max(i, length)

        return length


if __name__ == '__main__':
    solution = Solution()
    assert solution.longestConsecutive([9, 4, 5, 6, 3, 3, 6, 7, 90, 34, 23, 134, 67]) == 5
    assert solution.longestConsecutive([1]) == 1
    assert solution.longestConsecutive([]) == 0
