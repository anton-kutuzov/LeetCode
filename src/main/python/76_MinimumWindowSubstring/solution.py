"""LeetCode 76. Minimum Window Substring

https://leetcode.com/problems/minimum-window-substring/
"""

from __future__ import annotations

from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        have = 0
        need = len(t)

        if n < need:
            return ""

        frequency = defaultdict(int)
        for i in range(need):
            frequency[t[i]] += 1

        letter_to_count = defaultdict(int)
        left = 0
        right = 0
        min_left = 0
        min_right = float("infinity")

        while right < n:
            if s[right] in frequency:
                letter_to_count[s[right]] += 1
                if letter_to_count[s[right]] <= frequency[s[right]]:
                    have += 1

            while need == have:
                if s[left] in frequency:
                    letter_to_count[s[left]] -= 1
                    if letter_to_count[s[left]] < frequency[s[left]]:
                        have -= 1
                left += 1

                if (right - left) < (min_right - min_left):
                    min_right = right
                    min_left = left

            right += 1

        return s[min_left - 1:min_right + 1] if min_right != float("infinity") else ""
