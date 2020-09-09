package leetcode.linkedList.easy.DeleteNodeInALinkedList;

import leetcode.utils.list.ListNode;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        ListNode nodes = getNodes();
        solution.deleteNode(nodes);
        System.out.println(nodes);
    }

    private static ListNode getNodes() {
        int[] array = {1, 2, 7, 8, 9, 6, 10, 7};
        ListNode head = new ListNode(array[0]);
        ListNode curr = head;
        for (int i = 1; i < array.length; i++) {
            ListNode next = new ListNode(array[i]);
            curr.next = next;
            curr = curr.next;
        }
        return head.next;
    }
}
