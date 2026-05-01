class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if c == '*':
                stack.pop()
                continue
            stack.append(c)

        return "".join(stack)


if __name__ == '__main__':
    solution = Solution()
    assert solution.removeStars("lee**tco*de") == "ltcde"
