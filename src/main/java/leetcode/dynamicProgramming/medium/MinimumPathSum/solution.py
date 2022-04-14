from typing import List


class Solution:
    def min_path_sum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(1, n):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, m):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


solution = Solution()
print(solution.min_path_sum([[1, 3, 1],
                             [1, 5, 1],
                             [4, 2, 1]]))
print(solution.min_path_sum([[1, 2, 3],
                             [4, 5, 6]]))
print(solution.min_path_sum([[1]]))
print(solution.min_path_sum([[1], [1]]))
print(solution.min_path_sum([[1, 1]]))
print(solution.min_path_sum([[0]]))
