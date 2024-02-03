# https://leetcode.com/problems/maximum-binary-tree/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        max_deep = 0
        sum_val = 0

        def tree_loop(deep, root: Optional[TreeNode]):
            nonlocal max_deep
            nonlocal sum_val
            if root:
                if not root.left and not root.right:
                    if deep > max_deep:
                        max_deep = deep
                        sum_val = 0
                    if deep == max_deep:
                        sum_val += root.val
                tree_loop(deep + 1, root.left)
                tree_loop(deep + 1, root.right)
            return sum_val

        return tree_loop(0, root)


tree = TreeNode(1,
                TreeNode(2,
                         TreeNode(4,
                                  TreeNode(7)),
                         TreeNode(5)),
                TreeNode(3,
                         None,
                         TreeNode(6,
                                  None,
                                  TreeNode(8))))
solution = Solution()
print(solution.deepestLeavesSum(tree))  # 15
