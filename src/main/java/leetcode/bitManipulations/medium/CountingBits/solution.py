from typing import List


class Solution:
    def count_bits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            res.append(res[i // 2] + (i & 1))
        return res


solution = Solution()
print(solution.count_bits(5))
