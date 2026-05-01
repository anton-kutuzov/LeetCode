from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        length = len(s)
        num_parts = length // k
        last_part = length - num_parts * k

        result_str = []
        for part in range(0, num_parts):
            result_str.append(s[(part * k): ((part + 1) * k)])

        if last_part:
            result_str.append(s[num_parts * k:length] + fill * (k - last_part))

        return result_str


if __name__ == '__main__':
    solution = Solution()
    assert solution.divideString("abcdefghi", 3, "x") == ["abc", "def", "ghi"]
    assert solution.divideString("abcdefghij", 3, "x") == ["abc", "def", "ghi", "jxx"]
    assert solution.divideString("a", 5, "y") == ["ayyyy"]
