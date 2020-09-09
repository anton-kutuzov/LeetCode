package leetcode.tree.easy.MergeTwoBinaryTrees;


import leetcode.utils.tree.TreeNode;

/*
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of new tree.

Example:
Given:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Result:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7

Solution:
This is a recursive algorithms by two tree at one time. We use depth-first traversal
On each iteration if one of the tree is null then we return non null we go back. But if all trees not null we repeat operation:
1. Create new node
2. Go to the left subtree
2. Go to the right subtree
*/
public class Solution {
    public TreeNode mergeTree(TreeNode tree1, TreeNode tree2) {
        if (tree1 == null && tree2 != null) {
            return tree2;
        } else if (tree1 != null && tree2 == null) {
            return tree1;
        } else if (tree1 == null) {
            return null;
        }
        TreeNode treeNode = new TreeNode(tree1.getVal() + tree2.getVal());
        treeNode.setLeft(mergeTree(tree1.getLeft(), tree2.getLeft()));
        treeNode.setRight(mergeTree(tree1.getRight(), tree2.getRight()));
        return treeNode;
    }
}
