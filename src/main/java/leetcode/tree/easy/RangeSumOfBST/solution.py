# https://leetcode.com/problems/range-sum-of-bst/
# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range [low, high].

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        res = root.val if low <= root.val <= high else 0
        if root.left and root.val >= low:
            res += self.rangeSumBST(root.left, low, high)
        if root.right and root.val <= high:
            res += self.rangeSumBST(root.right, low, high)
        return res


tree = TreeNode(10,
                TreeNode(5,
                         TreeNode(3),
                         TreeNode(7)),
                TreeNode(15,
                         None,
                         TreeNode(18)))
solution = Solution()
print(solution.rangeSumBST(tree, 7, 15))


tree = TreeNode(10,
                TreeNode(5,
                         TreeNode(3, TreeNode(1)),
                         TreeNode(7, TreeNode(6))),
                TreeNode(15,
                         TreeNode(13),
                         TreeNode(18)))
solution = Solution()
print(solution.rangeSumBST(tree, 6, 10))
