---
id: 36
title: Valid Sudoku
slug: valid-sudoku
difficulty: medium
topics: [hashtable]
---

# [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

| Difficulty | Topic      | Solution                       |
|------------|------------|--------------------------------|
| 🟡 Medium  | Hash Table | [`solution.py`](./solution.py) |

## Problem

See the [original problem on LeetCode](https://leetcode.com/problems/valid-sudoku/).

## Examples

**1.** Input: `board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]`

Output: `true`

**2.** Input: `board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]`

Output: `false`

> Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top
> left 3x3 sub-box, it is invalid.

## Approach

<!-- Describe the idea in 2-4 sentences: data structure used, key invariant, why it works. -->

## Notes

<!-- Edge cases, alternative approaches, follow-ups. Delete this section if empty. -->
