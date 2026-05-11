"""LeetCode 9. Palindrome Number

https://leetcode.com/problems/palindrome-number/
"""

from __future__ import annotations


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        reverse = s[::-1]

        return s == reverse
