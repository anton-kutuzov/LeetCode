---
id: 1472
title: Design Browser History
slug: design-browser-history
difficulty: medium
topics: [stack]
---

# [1472. Design Browser History](https://leetcode.com/problems/design-browser-history/)

| Difficulty | Topic | Solution                       |
|------------|-------|--------------------------------|
| 🟡 Medium  | Stack | [`solution.py`](./solution.py) |

## Problem

See the [original problem on LeetCode](https://leetcode.com/problems/design-browser-history/).

## Examples

**1.** Input: `["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]`

Output:
`[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]`

> BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
> browserHistory.visit("google.com"); // You are in "leetcode.com". Visit "google.com"
> browserHistory.visit("facebook.com"); // You are in "google.com". Visit "facebook.com"
> browserHistory.visit("youtube.com"); // You are in "facebook.com". Visit "youtube.com"
> browserHistory.back(1); // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
> browserHistory.back(1); // You are in "facebook.com", move back to "google.com" return "google.com"
> browserHistory.forward(1); // You are in "google.com", move forward to "facebook.com" return "facebook.com"
> browserHistory.visit("linkedin.com"); // You are in "facebook.com". Visit "linkedin.com"
> browserHistory.forward(2); // You are in "linkedin.com", you cannot move forward any steps.
> browserHistory.back(2); // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com".
> return "google.com"
> browserHistory.back(7); // You are in "google.com", you can move back only one step to "leetcode.com". return "
> leetcode.com"

## Approach

<!-- Describe the idea in 2-4 sentences: data structure used, key invariant, why it works. -->

## Notes

<!-- Edge cases, alternative approaches, follow-ups. Delete this section if empty. -->
