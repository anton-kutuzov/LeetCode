class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for chart in s:
            if chart in brackets.values():
                stack.append(chart)
            else:
                if not stack or stack[-1] != brackets[chart]:
                    return False
                stack.pop()

        return not stack


if __name__ == '__main__':
    solution = Solution()
    assert solution.isValid(']') == False
    assert solution.isValid('}') == False
    assert solution.isValid(')') == False

    assert solution.isValid('[') == False
    assert solution.isValid('{') == False
    assert solution.isValid('(') == False

    assert solution.isValid('[]')
    assert solution.isValid('{}')
    assert solution.isValid('()')

    assert solution.isValid('(])') == False
    assert solution.isValid('(}') == False

    assert solution.isValid('([{}[]])')
