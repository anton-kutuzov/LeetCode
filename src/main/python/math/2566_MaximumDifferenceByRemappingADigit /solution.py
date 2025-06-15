class Solution:
    def minMaxDifference(self, num: int) -> int:
        cur = num
        n = 1
        while cur > 0:
            cur = cur // 10
            n *= 10

        cur = num
        cur_n = n // 10
        changed_int_min = None
        changed_int_max = None
        res_max = 0
        res_min = 0
        while cur_n > 0:
            cur_int = cur // cur_n
            if changed_int_min is None and cur_int > 0:
                changed_int_min = cur_int
            if changed_int_max is None and cur_int < 9:
                changed_int_max = cur_int
            if cur_int == changed_int_max:
                res_max = res_max * 10 + 9
            else:
                res_max = res_max * 10 + cur_int
            if cur_int == changed_int_min:
                res_min = res_min * 10
            else:
                res_min = res_min * 10 + cur_int
            cur = cur % cur_n
            cur_n //= 10
        return res_max - res_min


if __name__ == '__main__':
    solution = Solution()
    assert solution.minMaxDifference(100000000) == 900000000
    assert solution.minMaxDifference(11891) == 99009
    assert solution.minMaxDifference(90) == 99
    assert solution.minMaxDifference(1) == 9
    assert solution.minMaxDifference(9999) == 9999
