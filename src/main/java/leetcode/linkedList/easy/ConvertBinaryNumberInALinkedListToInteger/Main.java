package leetcode.linkedList.easy.ConvertBinaryNumberInALinkedListToInteger;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.getDecimalValue(getNodes()));
    }

    private static Solution.ListNode getNodes() {
        int[] array = {1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0};
        Solution.ListNode head = new Solution.ListNode(array[0]);
        Solution.ListNode curr = head;
        for (int i = 1; i < array.length; i++) {
            Solution.ListNode next = new Solution.ListNode(array[i]);
            curr.next = next;
            curr = curr.next;
        }
        return head;
    }
}
