from typing import List


class Solution:
    def lucky_numbers(self, matrix: List[List[int]]) -> List[int]:
        min_array = []
        max_array = []
        res = []

        for i in range(len(matrix)):
            min_el = matrix[i][0]
            for j in range(len(matrix[0])):
                if min_el > matrix[i][j]:
                    min_el = matrix[i][j]
            min_array.append(min_el)

        for j in range(len(matrix[0])):
            max_el = matrix[0][j]
            for i in range(len(matrix)):
                if max_el < matrix[i][j]:
                    max_el = matrix[i][j]
            max_array.append(max_el)

        for el in max_array:
            if el in min_array:
                res.append(el)

        return res


solution = Solution()
print(solution.lucky_numbers([[1, 2, 3],
                              [4, 7, 8],
                              [9, 11, 13],
                              [15, 16, 17]]))
