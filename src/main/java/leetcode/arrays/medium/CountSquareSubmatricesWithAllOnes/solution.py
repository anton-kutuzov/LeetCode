from typing import List


class Solution:
    def count_squares_2(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]) + 1

        return sum([sum(raw) for raw in matrix])

    def count_squares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        max_square_size = min(n, m)
        res = 0
        for raw in range(n):
            for column in range(m):
                for square_size in range(0, max_square_size):
                    if square_size + raw < n \
                            and square_size + column < m \
                            and self.is_check_matrix_ones(matrix, raw, column, square_size):
                        res += 1
                    else:
                        break

        return res

    def is_check_matrix_ones(self, matrix, raw, column, matrix_size):
        for i in range(raw, raw + matrix_size + 1):
            if matrix[i][column + matrix_size] == 0:
                return False
        for j in range(column, column + matrix_size):
            if matrix[raw + matrix_size][j] == 0:
                return False
        return True


solution = Solution()
print(solution.count_squares([
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 1, 1]
]))
print(solution.count_squares_2([
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 1, 1]
]))
