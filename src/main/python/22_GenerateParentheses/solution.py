from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def generate_parenthesis(open: int, close: int, s: str):
            if open + close == 2 * n:
                result.append(s)
                return

            if open < n:
                generate_parenthesis(open + 1, close, s + '(')

            if close < open:
                generate_parenthesis(open, close + 1, s + ')')

        generate_parenthesis(0, 0, "")

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))
