from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map_count = {}

        n = int(len(nums) / 2)

        for num in nums:
            if num in map_count:
                map_count[num] += 1
            else:
                map_count[num] = 1

            if map_count[num] > n:
                return num

        return -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.majorityElement([2, 3, 4, 5, 5, 5, 5]) == 5
