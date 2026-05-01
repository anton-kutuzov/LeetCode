---
id: 2375
title: Construct Smallest Number From DI String
slug: construct-smallest-number-from-di-string
difficulty: medium
topics: [stack]
---

# [2375. Construct Smallest Number From DI String](https://leetcode.com/problems/construct-smallest-number-from-di-string/)

| Difficulty | Topic | Solution                       |
|------------|-------|--------------------------------|
| 🟡 Medium  | Stack | [`solution.py`](./solution.py) |

## Problem

See the [original problem on LeetCode](https://leetcode.com/problems/construct-smallest-number-from-di-string/).

## Examples

**1.** Input: `pattern = "IIIDIDDD"`

Output: `"123549876"`

> At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
> At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
> Some possible values of num are "245639871", "135749862", and "123849765".
> It can be proven that "123549876" is the smallest possible num that meets the conditions.
> Note that "123414321" is not possible because the digit '1' is used more than once.

**2.** Input: `pattern = "DDD"`

Output: `"4321"`

> Some possible values of num are "9876", "7321", and "8742".
> It can be proven that "4321" is the smallest possible num that meets the conditions.

## Approach

<!-- Describe the idea in 2-4 sentences: data structure used, key invariant, why it works. -->

## Notes

<!-- Edge cases, alternative approaches, follow-ups. Delete this section if empty. -->
