from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        res = None
        sum_el = 0
        len_num = len(nums)
        while i < len_num and j < len_num:
            sum_el += nums[j]
            j += 1
            while sum_el >= target and i <= j:
                if (res is None or res > j - i) and sum_el >= target:
                    res = j - i
                sum_el -= nums[i]
                i += 1

        return 0 if res is None else res


if __name__ == '__main__':
    solution = Solution()
    print(solution.minSubArrayLen(5, [1, 1, 1, 1, 1, 3, 5, 7, 2]) == 1)
    print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2)
    print(solution.minSubArrayLen(5, [1]) == 0)
    print(solution.minSubArrayLen(5, []) == 0)
    print(solution.minSubArrayLen(5, [5]) == 1)
