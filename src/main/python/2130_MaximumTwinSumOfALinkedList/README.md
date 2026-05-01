---
id: 2130
title: Maximum Twin Sum of a Linked List
slug: maximum-twin-sum-of-a-linked-list
difficulty: medium
topics: [linkedlist]
---

# [2130. Maximum Twin Sum of a Linked List](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/)

| Difficulty | Topic | Solution                       |
|------------|-------|--------------------------------|
| 🟡 Medium  | Stack | [`solution.py`](./solution.py) |

## Problem

See the [original problem on LeetCode](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/).

## Examples

**1.** Input: `head = [5,4,2,1]`

Output: `6`

> Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
> There are no other nodes with twins in the linked list.
> Thus, the maximum twin sum of the linked list is 6.

**2.** Input: `head = [4,2,2,3]`

Output: `7`

> The nodes with twins present in this linked list are:

- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
  Thus, the maximum twin sum of the linked list is max(7, 4) = 7.

**3.** Input: `head = [1,100000]`

Output: `100001`

> There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.

## Approach

<!-- Describe the idea in 2-4 sentences: data structure used, key invariant, why it works. -->

## Notes

<!-- Edge cases, alternative approaches, follow-ups. Delete this section if empty. -->
