class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        current_number = 1
        result = ''
        for ch in pattern:
            if ch == 'D':
                stack.append(str(current_number))
            else:
                result += str(current_number)
                while stack:
                    result += stack.pop()
            current_number += 1

        result += str(current_number)
        while stack:
            result += stack.pop()

        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.smallestNumber("IIIDI") == "123546"