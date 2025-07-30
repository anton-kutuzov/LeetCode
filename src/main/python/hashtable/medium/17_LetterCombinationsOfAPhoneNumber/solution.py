from typing import List


class Solution:

    def letterCombinations(self, digits: str):

        digits_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []
        def combination(digit: str, comb: str):
            if not digit:
                return
            cur_letter = digit[:1]
            letters = digits_to_letters[cur_letter]
            for letter in letters:
                r = comb + letter
                if len(r) == len(digits):
                    res.append(r)
                combination(digit[1:], r)

        combination(digits, "")

        return res


if __name__ == '__main__':
    solution = Solution()
    solution.letterCombinations("23")