from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        min_el = prices[0]
        diff = 0
        for el in prices:
            if min_el > el:
                min_el = el
                continue
            diff = max(diff, el - min_el)
        return diff


solution = Solution()
print(solution.max_profit([7, 1, 5, 3, 6, 4]))
print(solution.max_profit([1, 2, 3, 4, 5]))
print(solution.max_profit([7, 6, 4, 3, 1]))
print(solution.max_profit([3, 20, 2, 5, 8, 4, 50, 3, 30, 10, 1, 100]))
print(solution.max_profit([3, 20, 2, 5, 8, 4, 50, 3, 30, 10, 100]))
print(solution.max_profit([3, 20, 2, 5, 8, 4, 50, 3, 30, 10, 1, 5]))
