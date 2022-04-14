from typing import List


class Solution:
    def next_greater_element(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num1 in nums1:
            i = nums2.index(num1)
            current = nums2[i]
            while 0 <= i < len(nums2) and num1 >= current:
                current = nums2[i]
                i += 1
            res.append(current if num1 < current else -1)
        return res


solution = Solution()
print(solution.next_greater_element([3, 1, 5, 7, 9, 2, 6], [1, 2, 3, 5, 6, 7, 9, 11]))
print(solution.next_greater_element([4, 1, 2], [1, 3, 4, 2]))
