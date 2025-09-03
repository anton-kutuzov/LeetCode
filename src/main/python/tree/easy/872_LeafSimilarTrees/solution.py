from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def go_by_tree_and_collect_leaf(root: Optional[TreeNode], leafs: set):
            if not root.right and not root.left:
                leafs.add(root.val)
                return

            go_by_tree_and_collect_leaf(root.left, leafs)
            go_by_tree_and_collect_leaf(root.right, leafs)


        leafs1 = set()
        leafs2 = set()

        go_by_tree_and_collect_leaf(root1, leafs1)
        go_by_tree_and_collect_leaf(root2, leafs2)

        return leafs1 == leafs2