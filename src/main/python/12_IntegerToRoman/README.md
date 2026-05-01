---
id: 12
title: Integer To Roman
slug: integer-to-roman
difficulty: medium
topics: [hashtable]
---

# [12. Integer To Roman](https://leetcode.com/problems/integer-to-roman/)

| Difficulty | Topic      | Solution                       |
|------------|------------|--------------------------------|
| 🟡 Medium  | Hash Table | [`solution.py`](./solution.py) |

## Problem

See the [original problem on LeetCode](https://leetcode.com/problems/integer-to-roman/).

## Examples

**1.** Input: `num = 3749`

Output: `"MMMDCCXLIX"`

> 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
> 700 = DCC as 500 (D) + 100 (C) + 100 (C)
> 40 = XL as 10 (X) less of 50 (L)
> 9 = IX as 1 (I) less of 10 (X)
> Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

**2.** Input: `num = 58`

Output: `"LVIII"`

> 50 = L
> 8 = VIII

**3.** Input: `num = 1994`

Output: `"MCMXCIV"`

> 1000 = M
> 900 = CM
> 90 = XC
> 4 = IV

## Approach

<!-- Describe the idea in 2-4 sentences: data structure used, key invariant, why it works. -->

## Notes

<!-- Edge cases, alternative approaches, follow-ups. Delete this section if empty. -->
