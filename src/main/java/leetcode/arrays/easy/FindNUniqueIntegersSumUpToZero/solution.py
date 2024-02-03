from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            return list(range(1, n // 2 + 1)) + list(range(-n // 2, 0))
        if n % 2 == 1:
            n = n - 1
            return list(range(1, n // 2 + 1)) + list(range(-n // 2, 0))


solution = Solution()
print(solution.sumZero(4))  # [1, 2, -2, -1]
print(solution.sumZero(2))  # [1, -1]
print(solution.sumZero(6))  # [1, 2, 3, -3, -2, -1]
print(solution.sumZero(8))  # [1, 2, 3, 4, -4, -3, -2, -1]
print()
print(solution.sumZero(3))
print(solution.sumZero(1))
print(solution.sumZero(5))
print(solution.sumZero(7))
