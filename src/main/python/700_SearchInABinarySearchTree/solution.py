# https://leetcode.com/problems/range-sum-of-bst/
# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range [low, high].

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)


tree = TreeNode(4,
                TreeNode(2,
                         TreeNode(1),
                         TreeNode(3)),
                TreeNode(7))
solution = Solution()
res = solution.searchBST(tree, 5)
print(res)
