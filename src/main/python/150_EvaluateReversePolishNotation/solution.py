from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        operations = {"+", "-", "*", "/"}
        for token in tokens:
            if token in operations:
                a = num_stack.pop()
                b = num_stack.pop()
                num_stack.append(self.calculate(b, a, token))
            else:
                num_stack.append(int(token))

        return num_stack.pop()

    @staticmethod
    def calculate(a, b, operation):
        if operation == '-':
            return a - b
        elif operation == '+':
            return a + b
        elif operation == '*':
            return a * b
        elif operation == '/':
            return int(a / b)
        raise Exception('invalid operation')


if __name__ == '__main__':
    solution = Solution()
    assert solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
