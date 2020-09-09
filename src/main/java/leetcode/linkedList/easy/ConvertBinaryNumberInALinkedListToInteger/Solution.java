package leetcode.linkedList.easy.ConvertBinaryNumberInALinkedListToInteger;


/*
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1.
The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.

Example:
Given:
head = [1,0,1]
Return:
5
Explanation: (101) in base 2 = (5) in base 10
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public static class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public int getDecimalValue(ListNode head) {
        ListNode node = head;
        int result = 0;
        int i = 0;
        while (node != null) {
            result = (result << 1) + node.val;
            node = node.next;
        }
        return result;
    }

    public int getDecimalValue2(ListNode head) {
        ListNode node = head;
        int result = 0;
        int i = 0;
        while (node.next != null) {
            ++i;
            node = node.next;
        }
        node = head;
        while (node != null) {
            result += (1 << i--) * node.val;
            node = node.next;
        }
        return result;
    }
}
