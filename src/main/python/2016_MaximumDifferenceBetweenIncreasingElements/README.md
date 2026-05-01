---
id: 2016
title: Maximum Difference Between Increasing Elements
slug: maximum-difference-between-increasing-elements
difficulty: easy
topics: [array]
---

# [2016. Maximum Difference Between Increasing Elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements/)

| Difficulty | Topic | Solution                       |
|------------|-------|--------------------------------|
| 🟢 Easy    | Array | [`solution.py`](./solution.py) |

## Problem

See the [original problem on LeetCode](https://leetcode.com/problems/maximum-difference-between-increasing-elements/).

## Examples

**1.** Input: `nums = [7,1,5,4]`

Output: `4`

> The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
> Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.

**2.** Input: `nums = [9,4,3,2]`

Output: `-1`

> There is no i and j such that i < j and nums[i] < nums[j].

**3.** Input: `nums = [1,5,2,10]`

Output: `9`

> The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.

## Approach

<!-- Describe the idea in 2-4 sentences: data structure used, key invariant, why it works. -->

## Notes

<!-- Edge cases, alternative approaches, follow-ups. Delete this section if empty. -->
