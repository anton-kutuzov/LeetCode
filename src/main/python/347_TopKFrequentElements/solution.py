from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res = set()
        for i in range(k):
            cur_max = 0
            cur_key_max = 0
            for key, val in counter.items():
                if val >= cur_max and key not in res:
                    cur_max = val
                    cur_key_max = key
            res.add(cur_key_max)
        return list(res)


if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(solution.topKFrequent([1], 1))
    print(solution.topKFrequent([1, 1, 1, 2, 2, 2, 3, 3, 3, 4], 3))
