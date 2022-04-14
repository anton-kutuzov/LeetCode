class Solution:
    def numberOfSteps(self, num: int) -> int:
        iterations = 0
        while num:
            if num & 1 == 0:
                num = num >> 1
            else:
                num -= 1
            iterations += 1
        return iterations


solution = Solution()
for i in range(1,100):
    print(f"{i} -> {solution.numberOfSteps(i)}")
print(solution.numberOfSteps(0))
print(solution.numberOfSteps(None))