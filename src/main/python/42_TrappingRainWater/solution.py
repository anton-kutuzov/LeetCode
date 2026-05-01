from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = 1
        sum_height = 0
        n = len(height)
        while j < n:

            sum_fill = 0
            sum_max_fill = 0
            max_right = height[j]
            max_j = j
            while j < n and height[i] > height[j]:
                sum_fill += height[j]
                if max_right <= height[j]:
                    max_right = height[j]
                    max_j = j
                    sum_max_fill = sum_fill
                j += 1

            if j < n:
                h = min(height[i], height[j])
                w = (j - i - 1)
                sum_height += h * w - sum_fill
            else:
                h = min(height[i], height[max_j])
                w = (max_j - i)
                sum_height += h * w - sum_max_fill

            i = j
            j += 1

        return sum_height


if __name__ == '__main__':
    solution = Solution()
    # assert solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert solution.trap([5, 4, 1, 2]) == 1
