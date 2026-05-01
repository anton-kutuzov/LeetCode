---
id: 2138
title: Divide a String Into Groups of Size K
slug: divide-a-string-into-groups-of-size-k
difficulty: easy
topics: [string]
---

# [2138. Divide a String Into Groups of Size K](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/)

| Difficulty | Topic  | Solution                       |
|------------|--------|--------------------------------|
| 🟢 Easy    | String | [`solution.py`](./solution.py) |

## Problem

See the [original problem on LeetCode](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/).

## Examples

**1.** Input: `s = "abcdefghi", k = 3, fill = "x"`

Output: `["abc","def","ghi"]`

> The first 3 characters "abc" form the first group.
> The next 3 characters "def" form the second group.
> The last 3 characters "ghi" form the third group.
> Since all groups can be completely filled by characters from the string, we do not need to use fill.
> Thus, the groups formed are "abc", "def", and "ghi".

**2.** Input: `s = "abcdefghij", k = 3, fill = "x"`

Output: `["abc","def","ghi","jxx"]`

> Similar to the previous example, we are forming the first three groups "abc", "def", and "ghi".
> For the last group, we can only use the character 'j' from the string. To complete this group, we add 'x' twice.
> Thus, the 4 groups formed are "abc", "def", "ghi", and "jxx".

## Approach

<!-- Describe the idea in 2-4 sentences: data structure used, key invariant, why it works. -->

## Notes

<!-- Edge cases, alternative approaches, follow-ups. Delete this section if empty. -->
