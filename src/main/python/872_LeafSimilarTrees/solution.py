from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def go_by_tree_and_collect_leaf(root: Optional[TreeNode], leafs: list):
            if not root.right and not root.left:
                leafs.append(root.val)
                return

            if root.left:
                go_by_tree_and_collect_leaf(root.left, leafs)
            if root.right:
                go_by_tree_and_collect_leaf(root.right, leafs)

        leafs1 = []
        leafs2 = []

        go_by_tree_and_collect_leaf(root1, leafs1)
        go_by_tree_and_collect_leaf(root2, leafs2)

        return leafs1 == leafs2


if __name__ == '__main__':
    solution = Solution()
    assert solution.leafSimilar(
        TreeNode(5, TreeNode(6), TreeNode(7)),
        TreeNode(8, TreeNode(6), TreeNode(7)),
    ) == True

    assert solution.leafSimilar(
        TreeNode(5, TreeNode(7), TreeNode(6)),
        TreeNode(8, TreeNode(6), TreeNode(7)),
    ) == False
