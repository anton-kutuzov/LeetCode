from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.loopCanJump(nums)

    # slow solution.py recursive solution.py
    def recurciveCanJump(self, nums, i) -> bool:
        if nums[i] + i >= len(nums) - 1:
            return True
        for j in range(1, nums[i] + 1):
            res = self.recurciveCanJump(nums, i + j)
            if res:
                return True
        return False

    def loopCanJump(self, nums: List[int]):
        n = len(nums)
        gold = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] + i >= gold:
                gold = i
        return gold == 0


if __name__ == '__main__':
    solution = Solution()
    assert solution.canJump([2, 2, 0, 1, 4])
    assert solution.canJump([2, 3, 1, 1, 4])
    assert solution.canJump([3, 2, 1, 0, 4]) == False
    assert solution.canJump([3])
    assert solution.canJump([1, 1])
    assert solution.canJump([1, 0])
    assert solution.canJump([2, 0, 0])
    assert solution.canJump([0, 1]) == False
    assert solution.canJump([1, 1, 1, 2, 0])
    assert solution.canJump([1, 1, 1, 0, 0]) == False
    assert solution.canJump([0])
    assert solution.canJump(
        [2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0,
         0, 3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0,
         7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6]) == False
