---
id: 1448
title: Count Good Nodes in Binary Tree
slug: count-good-nodes-in-binary-tree
difficulty: medium
topics: [tree]
---

# [1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

| Difficulty | Topic | Solution                       |
|------------|-------|--------------------------------|
| 🟡 Medium  | Tree  | [`solution.py`](./solution.py) |

## Problem

See the [original problem on LeetCode](https://leetcode.com/problems/count-good-nodes-in-binary-tree/).

## Examples

**1.** Input: `root = [3,1,4,3,null,1,5]`

Output: `4`

> Nodes in blue are good.
> Root Node (3) is always a good node.
> Node 4 -> (3,4) is the maximum value in the path starting from the root.
> Node 5 -> (3,4,5) is the maximum value in the path
> Node 3 -> (3,1,3) is the maximum value in the path.

**2.** Input: `root = [3,3,null,4,2]`

Output: `3`

> Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

**3.** Input: `root = [1]`

Output: `1`

> Root is considered as good.

## Approach

<!-- Describe the idea in 2-4 sentences: data structure used, key invariant, why it works. -->

## Notes

<!-- Edge cases, alternative approaches, follow-ups. Delete this section if empty. -->
