class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 1
        cur_k = k
        max_len = 0
        current_el = s[0]
        while i < j < len(s):

            if current_el != s[j] and cur_k <= 0:
                i = j - k - 1
                cur_k = k
                current_el = s[j]
                j = i

            if current_el == s[j]:
                j += 1
                max_len = max(max_len, j - i)
            elif current_el != s[j] and cur_k > 0:
                j += 1
                max_len = max(max_len, j - i)
                cur_k -= 1

        return max_len


if __name__ == '__main__':
    solution = Solution()
    # assert solution.characterReplacement("ABBBBBBBBBBBAAAAAAADAAAAAABADDDDDDDDBDDDDDDDDDBDDDDDDDD", 2) == 4
    assert solution.characterReplacement("AABABBA", 1) == 4
    assert solution.characterReplacement("ABAB", 2) == 4
    assert solution.characterReplacement("AAABAAABABBBBBBBBB", 2) == 12
