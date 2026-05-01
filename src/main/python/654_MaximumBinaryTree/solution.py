# https://leetcode.com/problems/maximum-binary-tree/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def construct_maximum_binary_tree(self, nums: List[int]) -> Optional[TreeNode]:

        def construct_maximum_binary_tree(start: int, end: int) -> Optional[TreeNode]:
            if end > start:
                i = self.find_max_index(nums, start, end)
                return TreeNode(nums[i],
                                construct_maximum_binary_tree(start, i),
                                construct_maximum_binary_tree(i + 1, end))

        return construct_maximum_binary_tree(0, len(nums))

    def find_max_index(self, nums: List[int], start: int, end: int):
        index = start
        for i in range(start, end):
            if nums[i] > nums[index]:
                index = i
        return index


solution = Solution()
tree = solution.construct_maximum_binary_tree([3, 2, 1, 6, 0, 5])
print(tree)
