from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_container = 0
        while i < j:
            container = min(height[i], height[j]) * (j - i)
            if max_container < container:
                max_container = container
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_container


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solution.maxArea([1, 1]) == 1
    assert solution.maxArea([1, 1, 5]) == 2
    assert solution.maxArea([5, 1, 2]) == 4
    assert solution.maxArea([5, 6, 2]) == 5
