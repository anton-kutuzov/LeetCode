# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = None
        current = None

        def reverse(old: Optional[ListNode]):
            nonlocal first
            nonlocal current
            if not old:
                return
            reverse(old.next)
            new = ListNode(old.val)
            if not first:
                first = new
                current = new
            else:
                current.next = new
                current = current.next

        reverse(head)

        return first
