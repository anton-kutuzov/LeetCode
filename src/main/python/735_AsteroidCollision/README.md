---
id: 735
title: Asteroid Collision
slug: asteroid-collision
difficulty: medium
topics: [stack]
---

# [735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)

| Difficulty | Topic | Solution                       |
|------------|-------|--------------------------------|
| 🟡 Medium  | Stack | [`solution.py`](./solution.py) |

## Problem

See the [original problem on LeetCode](https://leetcode.com/problems/asteroid-collision/).

## Examples

**1.** Input: `asteroids = [5,10,-5]`

Output: `[5,10]`

> The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

**2.** Input: `asteroids = [8,-8]`

Output: `[]`

> The 8 and -8 collide exploding each other.

**3.** Input: `asteroids = [10,2,-5]`

Output: `[10]`

> The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

**4.** Input: `asteroids = [3,5,-6,2,-1,4]​​​​​​​`

Output: `[-6,2,4]`

> The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2
> makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.

## Approach

<!-- Describe the idea in 2-4 sentences: data structure used, key invariant, why it works. -->

## Notes

<!-- Edge cases, alternative approaches, follow-ups. Delete this section if empty. -->
