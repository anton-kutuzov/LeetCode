class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alphanumeric(ch: str) -> bool:
            return "a" <= ch <= "z" or "A" <= ch <= "Z" or "0" <= ch <= "9"

        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not is_alphanumeric(s[i]):
                i += 1
            while i < j and not is_alphanumeric(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    solution = Solution()

    assert solution.isPalindrome("abccba") is True
    assert solution.isPalindrome("abcba") is True
    assert solution.isPalindrome("adcba") is False
    assert solution.isPalindrome("A man, a plan, a canal: Panama") is True
    assert solution.isPalindrome("race a car") is False
    assert solution.isPalindrome(" ") is True
    assert solution.isPalindrome("0P") is False
