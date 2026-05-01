---
id: 150
title: Evaluate Reverse Polish Notation
slug: evaluate-reverse-polish-notation
difficulty: medium
topics: [stack]
---

# [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

| Difficulty | Topic | Solution                       |
|------------|-------|--------------------------------|
| 🟡 Medium  | Stack | [`solution.py`](./solution.py) |

## Problem

See the [original problem on LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/).

## Examples

**1.** Input: `tokens = ["2","1","+","3","*"]`

Output: `9`

> ((2 + 1) * 3) = 9

**2.** Input: `tokens = ["4","13","5","/","+"]`

Output: `6`

> (4 + (13 / 5)) = 6

**3.** Input: `tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]`

Output: `22`

> ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
> = ((10 * (6 / (12 * -11))) + 17) + 5
> = ((10 * (6 / -132)) + 17) + 5
> = ((10 * 0) + 17) + 5
> = (0 + 17) + 5
> = 17 + 5
> = 22

## Approach

<!-- Describe the idea in 2-4 sentences: data structure used, key invariant, why it works. -->

## Notes

<!-- Edge cases, alternative approaches, follow-ups. Delete this section if empty. -->
