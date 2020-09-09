package leetcode.tree.easy.MergeTwoBinaryTrees;

import leetcode.utils.tree.TreeNode;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.mergeTree(getTreeNode1(), getTreeNode2()));
    }

    public static TreeNode getTreeNode1() {
        TreeNode treeNode1 = new TreeNode(1);
        TreeNode treeNode2 = new TreeNode(2);
        TreeNode treeNode3 = new TreeNode(3);
        TreeNode treeNode5 = new TreeNode(5);
        TreeNode treeNode6 = new TreeNode(6);
        treeNode3.setLeft(treeNode5);
        treeNode1.setLeft(treeNode3);
        treeNode1.setRight(treeNode2);
        treeNode5.setLeft(treeNode6);
        return treeNode1;
    }

    public static TreeNode getTreeNode2() {
        TreeNode treeNode2 = new TreeNode(2);
        TreeNode treeNode1 = new TreeNode(1);
        TreeNode treeNode4 = new TreeNode(4);
        TreeNode treeNode3 = new TreeNode(3);
        TreeNode treeNode7 = new TreeNode(7);
        TreeNode treeNode8 = new TreeNode(8);
        treeNode1.setRight(treeNode4);
        treeNode2.setLeft(treeNode1);
        treeNode2.setRight(treeNode3);
        treeNode3.setRight(treeNode7);
        treeNode3.setLeft(treeNode8);
        return treeNode2;
    }
}
