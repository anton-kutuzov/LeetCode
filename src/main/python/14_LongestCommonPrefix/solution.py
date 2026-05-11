"""LeetCode 14. Longest Common Prefix

https://leetcode.com/problems/longest-common-prefix/
"""

from __future__ import annotations

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(min(strs))
        max_pref = ""

        for i in range(min_len):
            cur = strs[0][i]
            for j in range(1, len(strs)):
                if cur != strs[j][i]:
                    return max_pref
            max_pref += strs[0][i]

        return max_pref
