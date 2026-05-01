# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        lst = self
        s = "["
        while lst:
            s += str(lst.val)
            s += "," if lst.next else ""
            lst = lst.next
        s += "]"
        return s


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode], n, res) -> Optional[ListNode]:
            if not l1 and not l2:
                if n > 0:
                    return ListNode(1)
                else:
                    return None

            r = n
            if l1:
                r += l1.val
            if l2:
                r += l2.val

            res.val = r % 10
            res.next = addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None, r // 10, ListNode())

            return res

        return addTwoNumbers(l1, l2, 0, ListNode())


solution = Solution()
res = solution.addTwoNumbers(ListNode(2, ListNode(4, ListNode(6))), ListNode(1, ListNode(5, ListNode(6, ListNode(9)))))
print(res)
