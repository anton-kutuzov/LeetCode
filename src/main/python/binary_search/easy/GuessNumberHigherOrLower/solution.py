# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0


def guess(num: int) -> int:
    if num > 7:
        return -1
    if num < 7:
        return 1
    return 0


class Solution:

    def guessNumber(self, n: int) -> int:
        def guessNumber(start: int, end: int) -> int:
            mid = (end + start) // 2
            g = guess(mid)
            if g == 0:
                return mid
            if g == -1:
                return guessNumber(start, mid - 1)
            if g == 1:
                return guessNumber(mid + 1, end)

        return guessNumber(1, n)

    def guessNumber2(self, n: int) -> int:

        start = 1
        end = n
        while True:
            mid = (end + start) // 2
            g = guess(mid)
            if g == 0:
                return mid
            if g == -1:
                end = mid - 1
            if g == 1:
                start = mid + 1


solution = Solution()
print(solution.guessNumber2(20))
