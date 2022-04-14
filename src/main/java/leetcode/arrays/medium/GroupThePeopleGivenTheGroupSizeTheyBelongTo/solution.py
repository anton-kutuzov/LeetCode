from typing import List


class Solution:
    def group_the_people(self, group_sizes: List[int]) -> List[List[int]]:
        dictionary = {}
        res = []
        for i, el in enumerate(group_sizes):
            if el not in dictionary:
                dictionary[el] = []
            dictionary[el].append(i)
            if len(dictionary[el]) == el:
                res.append(dictionary[el])
                dictionary[el] = []
        return res


solution = Solution()
print(solution.group_the_people([3, 3, 3, 3, 3, 1, 3]))
