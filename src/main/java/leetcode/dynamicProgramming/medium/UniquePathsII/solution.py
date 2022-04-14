from typing import List


class Solution:
    def unique_paths_with_obstacles(self, obstacle_grid: List[List[int]]) -> int:
        n = len(obstacle_grid)
        m = len(obstacle_grid[0])
        array = [[0] * m for _ in range(n)]

        for i in range(n):
            if obstacle_grid[i][0] == 1:
                break
            array[i][0] = 1
        for i in range(m):
            if obstacle_grid[0][i] == 1:
                break
            array[0][i] = 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacle_grid[i][j] != 1:
                    array[i][j] = array[i - 1][j] + array[i][j - 1]
        return array[-1][-1]


solution = Solution()
print(solution.unique_paths_with_obstacles([[0, 0, 0, 0, 0],
                                            [0, 0, 1, 0, 0],
                                            [0, 0, 1, 0, 0],
                                            [0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0]]))
print("22")
print()
print(solution.unique_paths_with_obstacles([[0, 1],
                                            [0, 0]]))
print("1")
print()
print(solution.unique_paths_with_obstacles([[0], [0]]))
print("1")
print()
print(solution.unique_paths_with_obstacles([[0]]))
print("1")
print()
print(solution.unique_paths_with_obstacles([[0, 0, 0],
                                            [0, 1, 0],
                                            [0, 0, 0]]))
print("2")
print()
print(solution.unique_paths_with_obstacles([[0, 0, 0],
                                            [0, 0, 0],
                                            [0, 0, 1]]))
print("0")
print()
print(solution.unique_paths_with_obstacles([[1, 0, 0],
                                            [0, 0, 0],
                                            [0, 0, 0]]))
print("0")
print()
print(solution.unique_paths_with_obstacles([[0, 0, 0],
                                            [0, 0, 0],
                                            [0, 0, 0]]))
print("6")
print()
print(solution.unique_paths_with_obstacles([[0, 0, 0],
                                            [0, 0, 1],
                                            [0, 1, 0]]))
print("0")
print()
print(solution.unique_paths_with_obstacles([[0, 0],
                                            [1, 1],
                                            [0, 0]]))
print("0")
print()
print(solution.unique_paths_with_obstacles([[1]]))
print("0")
