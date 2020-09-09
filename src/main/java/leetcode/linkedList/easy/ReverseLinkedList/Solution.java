package leetcode.linkedList.easy.ReverseLinkedList;


/*
Reverse a singly linked list.

Example:
Given: 1->2->3->4->5->NULL
Result: 5->4->3->2->1->NULL
*/

import leetcode.utils.list.ListNode;

class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode listNode = new ListNode();
        reverse(listNode, head);
        return listNode;
    }

    private ListNode reverse(ListNode revertHead, ListNode list) {
        if (list.getNext() == null) {
            revertHead.setVal(list.getVal());
            return revertHead;
        }
        ListNode result = reverse(revertHead, list.getNext());
        result.setNext(new ListNode(list.getVal()));
        return result.getNext();
    }
}
