package leetcode.tree.easy.ConvertSortedArrayToBinarySearchTree;


import leetcode.utils.tree.TreeNode;

/*
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given: [-10,-3,0,5,9],
Result: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

Solution:
We should do height-balanced binary tree for this reason we need two the approach as in QuickSort. It works because we have sorted array.
Using recursion we divide each part and find middle element and put in a tree as node. And it's guarantee us height-balanced binary tree.
*/
public class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 0) {
            return null;
        }
        return put(nums, null, 0, nums.length);
    }

    private TreeNode put(int[] nums, TreeNode tree, int start, int end) {
        if (start >= end) {
            return tree;
        }
        int mid = (start + end) / 2;
        tree = new TreeNode(nums[mid]);
        tree.left = put(nums, tree.left, start, mid);
        tree.right = put(nums, tree.right, mid + 1, end);
        return tree;
    }
}
