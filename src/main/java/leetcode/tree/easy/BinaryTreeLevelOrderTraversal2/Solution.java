package leetcode.tree.easy.BinaryTreeLevelOrderTraversal2;


import leetcode.utils.tree.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/*
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given: binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

Result: its bottom-up level order traversal as
[
  [15,7],
  [9,20],
  [3]
]

*/
public class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode node) {
        List<List<Integer>> lists = new ArrayList<>();
        levelOrderBottom(lists, 0, node);
        return lists;
    }

    private void levelOrderBottom(List<List<Integer>> list, int level, TreeNode tree) {
        if (tree == null) {
            return;
        }
        if (list.size() <= level) {
            list.add(0, new ArrayList<>());
        }
        levelOrderBottom(list, level + 1, tree.left);
        levelOrderBottom(list, level + 1, tree.right);
        list.get(list.size() - 1 - level).add(tree.val);
    }
}
