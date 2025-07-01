class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isAlphabetic(ch: str):
            return 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'

        i = 0
        j = len(s) - 1
        while i < j:

            while not isAlphabetic(s[i]):
                i += 1

            while not isAlphabetic(s[j]):
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True


if __name__ == '__main__':
    solution = Solution()

    assert solution.isPalindrome("abccba") == True
    assert solution.isPalindrome("abcba") == True
    assert solution.isPalindrome("adcba") == False
