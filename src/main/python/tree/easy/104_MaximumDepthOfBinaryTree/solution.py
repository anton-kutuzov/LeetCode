from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        max_depth = 0
        def go_by_tree(node: Optional[TreeNode], current: int):
            nonlocal max_depth
            if not node:
                max_depth = max(max_depth, current)
                return
            go_by_tree(node.left, current + 1)
            go_by_tree(node.right, current + 1)

        go_by_tree(root, 0)
        return max_depth


    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        h = self.maxDepth2(root.left)
        l = self.maxDepth2(root.right)
        return 1 + max(h, l)