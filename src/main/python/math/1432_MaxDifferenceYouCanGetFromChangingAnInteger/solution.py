class Solution:
    def maxDiff(self, num: int) -> int:
        size = 1
        numeral = num
        while numeral > 0:
            numeral = numeral // 10
            size *= 10

        size //= 10
        numeral = num
        max_numeral = None
        min_numeral = None
        res_max = 0
        res_min = 0
        min_replacer = 0
        cur_size = size
        while cur_size > 0:
            cur_el = int(numeral // cur_size)
            if max_numeral is None and cur_el < 9:
                max_numeral = cur_el
            if min_numeral is None and cur_el > 1:
                min_numeral = cur_el
                min_replacer = 1 if cur_size == size else 0
            if cur_el == max_numeral:
                res_max *= 10
                res_max += 9
            else:
                res_max *= 10
                res_max += cur_el
            if cur_el == min_numeral:
                res_min *= 10
                res_min += min_replacer
            else:
                res_min *= 10
                res_min += cur_el

            numeral %= cur_size
            cur_size //= 10

        return res_max - res_min


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxDiff(123456) == (923456 - 103456)
    assert solution.maxDiff(100000000) == (900000000 - 100000000)
    assert solution.maxDiff(11891) == (99899 - 11091)
    assert solution.maxDiff(90) == (99 - 10)
    assert solution.maxDiff(1) == (9 - 1)
    assert solution.maxDiff(9999) == (9999 - 1111)
