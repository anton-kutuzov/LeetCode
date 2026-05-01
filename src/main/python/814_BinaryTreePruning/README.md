---
id: 814
title: Binary Tree Pruning
slug: binary-tree-pruning
difficulty: medium
topics: [tree]
---

# [814. Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/)

| Difficulty | Topic | Solution                       |
|------------|-------|--------------------------------|
| 🟡 Medium  | Tree  | [`solution.py`](./solution.py) |

## Problem

See the [original problem on LeetCode](https://leetcode.com/problems/binary-tree-pruning/).

## Examples

**1.** Input: `root = [1,null,0,0,1]`

Output: `[1,null,0,null,1]`

> Only the red nodes satisfy the property "every subtree not containing a 1".
> The diagram on the right represents the answer.

**2.** Input: `root = [1,0,1,0,0,0,1]`

Output: `[1,null,1,null,1]`

**3.** Input: `root = [1,1,0,1,1,0,1,0]`

Output: `[1,1,0,1,1,null,1]`

## Approach

<!-- Describe the idea in 2-4 sentences: data structure used, key invariant, why it works. -->

## Notes

<!-- Edge cases, alternative approaches, follow-ups. Delete this section if empty. -->
