from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDictSet = set(wordDict)
        indexMap = {}
        for i in range(0, len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDictSet:
                    if i in indexMap:
                        indexMap[i].append(j)
                    else:
                        indexMap[i] = [j]

        cache = {}

        def isBreaked(index: int):
            if index == len(s):
                return True
            if index in cache:
                return cache[index]
            if index not in indexMap:
                cache[index] = False
                return False
            cache[index] = any(isBreaked(next_index) for next_index in indexMap[index])
            return cache[index]

        return isBreaked(0)


if __name__ == '__main__':
    solution = Solution()
    assert solution.wordBreak("catsandog", ["c", "at", "dog", "cats", "an"])
