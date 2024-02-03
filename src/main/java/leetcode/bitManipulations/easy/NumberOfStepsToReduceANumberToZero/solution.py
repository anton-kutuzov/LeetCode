from typing import List


class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num <= 0:
            return 0
        count = 0
        while num > 0:
            count += (1 + num % 2)
            num >>= 1
        return count - 1


solution = Solution()
print(solution.numberOfSteps(0))  # 0
print(solution.numberOfSteps(1))  # 1
print(solution.numberOfSteps(14))  # 6
print(solution.numberOfSteps(8))  # 4
print(solution.numberOfSteps(123))  # 12
