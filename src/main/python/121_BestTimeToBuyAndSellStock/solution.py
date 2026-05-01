from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        buy = prices[0]
        for price in prices[1:]:
            result = max(result, price - buy)
            buy = min(buy, price)

        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
