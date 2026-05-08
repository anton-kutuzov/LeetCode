---
id: 76
title: Minimum Window Substring
slug: minimum-window-substring
difficulty: hard
topics: [hashtable]
---

# [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

| Difficulty | Topics | Solution |
| --- | --- | --- |
| 🔴 Hard | Hash Table, String, Sliding Window | [`solution.py`](./solution.py) |

## Problem

Given two strings `s` and `t` of lengths `m` and `n` respectively, return *the **minimum window*** ***substring**** of *`s`* such that every character in *`t`* (**including duplicates**) is included in the window*. If there is no such substring, return *the empty string *`""`.

The testcases will be generated such that the answer is **unique**.

## Examples

**1.** Input: `s = "anbcnndannnbcdnaaaa", t = "abc"`

Output: `"anbc"`

**Constraints:**

	
- `m == s.length`
	
- `n == t.length`
	
- `1 <= m, n <= 10^5`
	
- `s` and `t` consist of uppercase and lowercase English letters.

 

**Follow up:** Could you find an algorithm that runs in `O(m + n)` time?

## Approach

<!-- Describe the idea in 2-4 sentences. -->
