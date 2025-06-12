from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.b_search(nums, 0, len(nums) - 1)

    def b_search(self, nums, l, r):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
        return nums[l]


if __name__ == '__main__':
    solution = Solution()
    assert solution.findMin([9, 10, 11, 12, 5, 6, 7, 8]) == 5
    assert solution.findMin([6, 7, 8, 9, 10, 11, 12, 5]) == 5
    assert solution.findMin([12, 5, 6, 7, 8, 9, 10, 11]) == 5
    assert solution.findMin([11, 12, 5, 6, 7, 8, 9, 10]) == 5
    assert solution.findMin([5, 6, 7, 8, 9, 10, 11, 12]) == 5
    assert solution.findMin([1]) == 1
