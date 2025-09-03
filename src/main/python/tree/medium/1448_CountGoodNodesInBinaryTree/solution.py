# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count_good_nodes = 0

        def go_by_tree(node: TreeNode, max_value: int):
            nonlocal count_good_nodes
            if not node:
                return
            if node.val >= max_value:
                count_good_nodes += 1
            go_by_tree(node.left, max(max_value, node.val))
            go_by_tree(node.right, max(max_value, node.val))

        go_by_tree(root, root.val)