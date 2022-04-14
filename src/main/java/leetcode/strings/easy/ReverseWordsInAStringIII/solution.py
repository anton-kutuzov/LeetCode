class Solution:
    def reverse_words(self, s: str) -> str:
        words = s.split()
        return " ".join([word[::-1] for word in words])


solution = Solution()
print(solution.reverse_words("Let's take LeetCode contest"))
