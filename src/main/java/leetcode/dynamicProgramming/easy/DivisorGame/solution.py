class Solution:
    def divisor_game(self, n: int) -> bool:
        return n % 2 == 0


solution = Solution()
print(solution.divisor_game(6))
print(solution.divisor_game(3))
print(solution.divisor_game(2))