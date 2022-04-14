from collections import Counter
from typing import List


class Solution:
    def repeated_n_times(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for el in counter:
            if counter[el] > 1:
                return el


solution = Solution()
print(solution.repeated_n_times([5, 1, 5, 2, 5, 3, 5, 4]))
