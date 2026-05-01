# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def walk_tree(node, path):
            if not node:
                return 0

            count = 0
            path.append(node.val)
            curr_sum = 0
            for el in reversed(path):
                curr_sum += el
                if curr_sum == targetSum:
                    count += 1

            count += walk_tree(node.left, path)
            count += walk_tree(node.right, path)
            path.pop()
            return count

        return walk_tree(root, [])


if __name__ == '__main__':
    solution = Solution()

    root = TreeNode(10,
                    TreeNode(5,
                             TreeNode(3,
                                      TreeNode(3),
                                      TreeNode(-2)),
                             TreeNode(2,
                                      None,
                                      TreeNode(1))),
                    TreeNode(-3, None, TreeNode(11)))

    assert solution.pathSum(root, 8) == 3
