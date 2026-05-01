# https://leetcode.com/problems/insert-into-a-binary-search-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insert_into_BST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        node = TreeNode(root.val)
        if val <= root.val:
            node.right = root.right
            node.left = self.insert_into_BST(root.left, val)
        if val > root.val:
            node.left = root.left
            node.right = self.insert_into_BST(root.right, val)
        return node


tree = TreeNode(4,
                TreeNode(2,
                         TreeNode(1),
                         TreeNode(3)),
                TreeNode(7))
solution = Solution()
res = solution.insert_into_BST(tree, 5)
print(res)
