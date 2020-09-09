package leetcode.linkedList.easy.ReverseLinkedList;

import leetcode.utils.list.ListNode;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.reverseList(getNodes()));
    }

    private static ListNode getNodes() {
        int[] array = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        ListNode head = new ListNode(array[0]);
        ListNode curr = head;
        for (int i = 1; i < array.length; i++) {
            ListNode next = new ListNode(array[i]);
            curr.setNext(next);
            curr = curr.getNext();
        }
        return head;
    }
}
