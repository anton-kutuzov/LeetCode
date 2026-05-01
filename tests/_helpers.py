"""Helpers for converting between LeetCode test inputs and the Python data
structures used by `Solution` methods (linked lists, binary trees, ...)."""

from __future__ import annotations

from collections import deque
from typing import Any


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def make_linked_list(values: list[int]) -> ListNode | None:
    head: ListNode | None = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def linked_list_to_list(head: ListNode | None) -> list[int]:
    out: list[int] = []
    node = head
    while node is not None:
        out.append(node.val)
        node = node.next
    return out


def make_tree(values: list[Any]) -> TreeNode | None:
    """Build a binary tree from level-order list (LeetCode style, with `None`
    for missing children).
    """
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue: deque[TreeNode] = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root
