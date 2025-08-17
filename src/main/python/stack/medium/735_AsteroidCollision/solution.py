from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack) >= 2 and stack[-1] < 0:
                asteroid_right = stack.pop()
                asteroid_left = stack.pop()
                if abs(asteroid_left) > abs(asteroid_right):
                    stack.append(asteroid_left)
                elif abs(asteroid_left) < abs(asteroid_right):
                    stack.append(asteroid_right)

        return stack


if __name__ == '__main__':
    solution = Solution()
    assert solution.asteroidCollision([-2, -1, 1, 2]) == []
    assert solution.asteroidCollision([8, -8]) == []
    assert solution.asteroidCollision([10, 2, -5]) == [10]
    assert solution.asteroidCollision([10, -5, 5, -7, 9, -3, 2]) == [10, 9, 2]
