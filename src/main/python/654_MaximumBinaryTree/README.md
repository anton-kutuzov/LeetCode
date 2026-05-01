---
id: 654
title: Maximum Binary Tree
slug: maximum-binary-tree
difficulty: medium
topics: [tree]
---

# [654. Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/)

| Difficulty | Topic | Solution                       |
|------------|-------|--------------------------------|
| 🟡 Medium  | Tree  | [`solution.py`](./solution.py) |

## Problem

See the [original problem on LeetCode](https://leetcode.com/problems/maximum-binary-tree/).

## Examples

**1.** Input: `nums = [3,2,1,6,0,5]`

Output: `[6,3,5,null,2,0,null,null,1]`

> The recursive calls are as follow:

- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.

**2.** Input: `nums = [3,2,1]`

Output: `[3,null,2,null,1]`

## Approach

<!-- Describe the idea in 2-4 sentences: data structure used, key invariant, why it works. -->

## Notes

<!-- Edge cases, alternative approaches, follow-ups. Delete this section if empty. -->
