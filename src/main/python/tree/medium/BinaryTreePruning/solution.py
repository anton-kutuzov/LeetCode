# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def deep_loop(root: Optional[TreeNode]):
            if root.left:
                root.left = deep_loop(root.left)
            if root.right:
                root.right = deep_loop(root.right)
            if root.val == 0 and not root.right and not root.left:
                return None
            return root

        return deep_loop(root)


tree = TreeNode(1,
                TreeNode(0,
                         TreeNode(0),
                         TreeNode(1,
                                  TreeNode(0),
                                  TreeNode(0))),
                TreeNode(0,
                         TreeNode(1),
                         TreeNode(1,
                                  TreeNode(0),
                                  TreeNode(1))))
solution = Solution()
res = solution.pruneTree(tree)
print(res)


tree2 = TreeNode(1,
                TreeNode(0,
                         TreeNode(0),
                         TreeNode(0)),
                TreeNode(1,
                         TreeNode(0),
                         TreeNode(1)))
res2 = solution.pruneTree(tree2)
print(res2)