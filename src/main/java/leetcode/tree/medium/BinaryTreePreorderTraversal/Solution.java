package leetcode.tree.medium.ConvertSortedListToBinarySearchTree;


import leetcode.utils.list.ListNode;
import leetcode.utils.tree.TreeNode;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Collections;

/*
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
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
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) {
            return null;
        }
        return put(head, null, 0, size(head));
    }

    private TreeNode put(ListNode node, TreeNode tree, int start, int end) {
        if (start >= end) {
            return tree;
        }
        int mid = (start + end) / 2;
        ListNode midNode = findMid(node, mid - start);
        tree = new TreeNode(midNode.val);
        tree.left = put(node, tree.left, start, mid);
        tree.right = put(midNode.next, tree.right, mid + 1, end);
        return tree;
    }

    private static ListNode findMid(ListNode node, int size) {
        for (int i = 0; i < size; i++) {
            node = node.next;
        }
        return node;
    }

    private static int size(ListNode node) {
        int size = 0;
        while (node != null) {
            node = node.next;
            size++;
        }
        return size;
    }
}
