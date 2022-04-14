from functools import lru_cache


class Solution:
    def num_decodings(self, s: str) -> int:

        @lru_cache(None)
        def num_decodings(s: str, i: int) -> int:
            if i >= len(s):
                return 1
            res = 0
            if int(s[i]):
                res += num_decodings(s, i + 1)
            if 10 <= int(s[i:i + 2]) <= 26:
                res += num_decodings(s, i + 2)

            return res

        return num_decodings(s, 0) if s else 0


solution = Solution()
print(solution.num_decodings("11106"))
print(solution.num_decodings("12"))
print(solution.num_decodings("226"))
print(solution.num_decodings("06"))
print(solution.num_decodings("1"))
print(solution.num_decodings("30"))
print(solution.num_decodings(""))
print(solution.num_decodings("26"))
print(solution.num_decodings("2626"))
print(solution.num_decodings("111111111111111111111111111111111111111111111"))
