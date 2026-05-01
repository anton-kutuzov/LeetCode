from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:

            cur_sum = numbers[left] + numbers[right]
            if cur_sum == target:
                return [left + 1, right + 1]
            elif cur_sum > target:
                right -= 1
            else:
                left += 1

        return []


if __name__ == '__main__':
    solution = Solution()

    assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert solution.twoSum([2, 7, 11, 15], 13) == [1, 3]
    assert solution.twoSum([2, 7, 11, 15], 26) == [3, 4]
    assert solution.twoSum([2, 7, 11, 15], 18) == [2, 3]
