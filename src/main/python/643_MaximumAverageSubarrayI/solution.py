from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        res_avg = current_sum / k
        j = 0
        for i in range(k, len(nums)):
            current_sum -= nums[j]
            j += 1
            current_sum += nums[i]

            if (current_sum / k) > res_avg:
                res_avg = current_sum / k

        return res_avg

if __name__ == '__main__':
    solution = Solution()
    solution.findMaxAverage([1,12,-5,-6,50,3], 4)
