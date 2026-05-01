---
id: 2390
title: Removing Stars From a String
slug: removing-stars-from-a-string
difficulty: medium
topics: [ stack ]
---

# [2390. Removing Stars From a String](https://leetcode.com/problems/removing-stars-from-a-string/)

| Difficulty | Topic | Solution                       |
|------------|-------|--------------------------------|
| 🟡 Medium  | Stack | [`solution.py`](./solution.py) |

## Problem

See the [original problem on LeetCode](https://leetcode.com/problems/removing-stars-from-a-string/).

## Examples

**1.** Input: `s = "leet**cod*e"`

Output: `"lecoe"`

> Performing the removals from left to right:

- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
  There are no more stars, so we return "lecoe".

**2.** Input: `s = "erase*****"`

Output: `""`

> The entire string is removed, so we return an empty string.

## Approach

<!-- Describe the idea in 2-4 sentences: data structure used, key invariant, why it works. -->

## Notes

<!-- Edge cases, alternative approaches, follow-ups. Delete this section if empty. -->
