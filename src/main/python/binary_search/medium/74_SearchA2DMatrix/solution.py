from operator import truediv
from typing import List
from unittest.util import sorted_list_difference

from setuptools.command.egg_info import manifest_maker


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left = 0
        right = n * m - 1

        while left <= right:
            mid = left + (right - left) // 2

            mid_i = mid // n
            mid_j = mid - mid_i * n

            if matrix[mid_i][mid_j] == target:
                return True
            if matrix[mid_i][mid_j] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


if __name__ == '__main__':
    solution = Solution()
    assert solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
    assert solution.searchMatrix([[1]], 1)
