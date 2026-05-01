from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        num_of_balls_left = 0
        num_of_balls_right = 0
        n = len(boxes) - 1
        right_to_left = [0] * (n + 1)
        left_to_right = [0] * (n + 1)
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            if boxes[i - 1] == '1':
                num_of_balls_left += 1
            if boxes[n - i + 1] == '1':
                num_of_balls_right += 1

            right_to_left[i] = right_to_left[i - 1] + num_of_balls_left
            left_to_right[n - i] = left_to_right[n - i + 1] + num_of_balls_right

        for i in range(0, n + 1):
            result[i] = right_to_left[i] + left_to_right[i]

        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.minOperations("110") == [1, 1, 3]
