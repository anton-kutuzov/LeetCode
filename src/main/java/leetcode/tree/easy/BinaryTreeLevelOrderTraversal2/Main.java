package leetcode.tree.easy.BinaryTreeLevelOrderTraversal2;

import leetcode.utils.tree.TreeNode;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.levelOrderBottom(getTreeNode1()));
        System.out.println(solution.levelOrderBottom(getTreeNode2()));
        System.out.println(solution.levelOrderBottom(new TreeNode(5)));
    }

    public static TreeNode getTreeNode1() {
        TreeNode treeNode1 = new TreeNode(3);
        TreeNode treeNode2 = new TreeNode(9);
        TreeNode treeNode3 = new TreeNode(20);
        TreeNode treeNode5 = new TreeNode(15);
        TreeNode treeNode6 = new TreeNode(7);
        treeNode1.setLeft(treeNode2);
        treeNode1.setRight(treeNode3);
        treeNode3.setLeft(treeNode5);
        treeNode3.setRight(treeNode6);
        return treeNode1;
    }

    public static TreeNode getTreeNode2() {
        TreeNode treeNode1 = new TreeNode(3);
        TreeNode treeNode2 = new TreeNode(9);
        TreeNode treeNode3 = new TreeNode(20);
        TreeNode treeNode4 = new TreeNode(15);
        TreeNode treeNode5 = new TreeNode(7);
        treeNode1.setLeft(treeNode2);
        treeNode2.setLeft(treeNode3);
        treeNode3.setLeft(treeNode4);
        treeNode3.setRight(treeNode5);
        return treeNode1;
    }
}
