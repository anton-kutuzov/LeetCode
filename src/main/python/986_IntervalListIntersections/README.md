---
id: 986
title: Interval List Intersections
slug: interval-list-intersections
difficulty: medium
topics: [ two_points ]
---

# [986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)

| Difficulty | Topics                          | Solution                       |
|------------|---------------------------------|--------------------------------|
| 🟡 Medium  | Array, Two Pointers, Sweep Line | [`solution.py`](./solution.py) |

## Problem

You are given two lists of closed intervals, `firstList` and `secondList`, where `firstList[i] = [start_i, end_i]` and
`secondList[j] = [start_j, end_j]`. Each list of intervals is pairwise **disjoint** and in **sorted order**.

Return *the intersection of these two interval lists*.

A **closed interval** `[a, b]` (with `a <= b`) denotes the set of real numbers `x` with `a <= x <= b`.

The **intersection** of two closed intervals is a set of real numbers that are either empty or represented as a closed
interval. For example, the intersection of `[1, 3]` and `[2, 4]` is `[2, 3]`.

## Examples

**1.** Input: `firstList = [[1,4], [6,8], [9,12]], secondList = [[2,4], [5,7], [12,13]]`

Output: `[[2,4], [6,7], [12,12]]`

**Constraints:**

- `0 <= firstList.length, secondList.length <= 1000`

- `firstList.length + secondList.length >= 1`

- `0 <= start_i < end_i <= 10^9`

- `end_i < start_i+1`

- `0 <= start_j < end_j <= 10^9 `

- `end_j < start_j+1`

## Approach

<!-- Describe the idea in 2-4 sentences. -->
