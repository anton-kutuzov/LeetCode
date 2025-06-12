class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sing = -1 if x < 0 else 1
        x = abs(x)
        max_res = 1 << 31
        while x > 0:
            cur = x % 10
            res *= 10
            res += cur
            x = x // 10
            if res > max_res:
                return 0
        return sing * res


if __name__ == '__main__':
    solution = Solution()
    assert solution.reverse(123) == 321
    assert solution.reverse(1) == 1
    assert solution.reverse(-1) == -1
    assert solution.reverse(0) == 0
    assert solution.reverse(29292) == 29292
    assert solution.reverse(55) == 55
    assert solution.reverse(120) == 21
    assert solution.reverse(1534236469) == 0
    assert solution.reverse(2147483647) == 0
    assert solution.reverse(-2147483647) == 0
    assert solution.reverse(1563847412) == 0
