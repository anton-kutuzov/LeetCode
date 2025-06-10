package leetcode.tree.medium.ConvertSortedListToBinarySearchTree;

import leetcode.utils.list.ListNode;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.sortedListToBST(getNodes(new int[]{0, 1, 2, 3, 4, 5})));
    }

    private static ListNode getNodes(int[] array) {
        ListNode head = new ListNode(array[0]);
        ListNode curr = head;
        for (int i = 1; i < array.length; i++) {
            ListNode next = new ListNode(array[i]);
            curr.next = next;
            curr = curr.next;
        }
        return head;
    }
}
