class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_map = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        n = len(s)
        res = 0
        i = 0
        while i < n:

            if i != n - 1 and s[i:i + 2] in roman_to_int_map:
                res += roman_to_int_map[s[i:i + 2]]
                i += 2
            else:
                res += roman_to_int_map[s[i]]
                i += 1

        return res

    def romanToInt2(self, s: str) -> int:
        roman_to_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = len(s)
        res = 0
        i = 0
        while i < n:

            if i < n - 1 and roman_to_int_map[s[i]] < roman_to_int_map[s[i + 1]]:
                res -= roman_to_int_map[s[i]]
            else:
                res += roman_to_int_map[s[i]]

            i += 1

        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.romanToInt("MCMXCIV") == 1994
    assert solution.romanToInt("III") == 3
    assert solution.romanToInt("VIII") == 8
    assert solution.romanToInt("IV") == 4

    assert solution.romanToInt2("MCMXCIV") == 1994
    assert solution.romanToInt2("III") == 3
    assert solution.romanToInt2("VIII") == 8
    assert solution.romanToInt2("IV") == 4
