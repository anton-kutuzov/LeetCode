class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = {1: 'I',
                          5: 'V',
                          10: 'X',
                          50: 'L',
                          100: 'C',
                          500: 'D',
                          1000: 'M'}
        res = ''
        power = 1
        i = num
        while i > 0:
            i = i // 10
            power *= 10

        power = power // 10
        i = num
        while power > 0:

            number = i // power

            if number < 4:
                res += roman_numerals[power] * number
            elif number == 4 or number == 9:
                res += roman_numerals[power] + roman_numerals[(number + 1) * power]
            elif 4 < number < 9 and number != 5:
                res += roman_numerals[5 * power] + roman_numerals[power] * (number - 5)
            else:
                res += roman_numerals[number * power]

            i = i % power
            power = power // 10

        return res

    def intToRoman2(self, num: int) -> str:
        roman_numerals = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        res = ''
        for k, v in roman_numerals:
            if num == 0:
                break
            count = num // k
            res += v * count
            num -= k * count

        return res

if __name__ == '__main__':
    solution = Solution()
    assert solution.intToRoman(3979) == 'MMMCMLXXIX'
    assert solution.intToRoman(3959) == 'MMMCMLIX'

    assert solution.intToRoman2(3979) == 'MMMCMLXXIX'
    assert solution.intToRoman2(3959) == 'MMMCMLIX'