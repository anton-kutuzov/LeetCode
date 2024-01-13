from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_sum = [sum(a) for a in mat]
        column_sum = [sum(a) for a in zip(*mat)]

        count = 0
        for i in range(len(mat)):
            if row_sum[i] == 1:
                for j in range(len(mat[0])):
                    if mat[i][j] == 1 and column_sum[j] == 1:
                        count += 1

        return count


solution = Solution()
print(solution.numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]]))  # 1
print(solution.numSpecial([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))  # 3
print(solution.numSpecial([[1, 1, 1], [0, 0, 1], [1, 0, 0]]))  # 0
print(solution.numSpecial([[0, 1, 0], [0, 1, 0], [0, 1, 1], [1, 0, 0]]))  # 1
print(solution.numSpecial([[0, 1, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0]]))  # 2
