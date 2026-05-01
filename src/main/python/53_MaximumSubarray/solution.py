from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        j = 1
        sum_el = nums[0]
        max_sum = nums[0]
        while j < len(nums):

            sum_el += nums[j]

            sum_subarr = 0
            k = i
            while k < j:
                sum_subarr += nums[k]
                if sum_el < sum_el - sum_subarr:
                    sum_el -= sum_subarr
                    i = k + 1
                k += 1

            if max_sum < sum_el:
                max_sum = sum_el

            j += 1

        return max_sum


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert solution.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert solution.maxSubArray([1]) == 1
    assert solution.maxSubArray([23, 1, -3, 4, -1, 2, 1, -5, 4]) == 1
