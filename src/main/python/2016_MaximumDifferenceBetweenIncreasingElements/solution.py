from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_el = nums[0]
        min_index = 0
        max_diff = -1
        i = 1
        n = len(nums)
        while min_index < i < n:
            if min_el > nums[i]:
                min_index = i
                min_el = nums[i]
            elif max_diff < nums[i] - min_el and nums[i] > min_el:
                max_diff = nums[i] - min_el
            i += 1
        return max_diff


if __name__ == '__main__':
    solution = Solution()
    assert solution.maximumDifference([7, 1, 5, 4]) == 4
    assert solution.maximumDifference([6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 1]) == 5
    assert solution.maximumDifference([3, 5, 2, 10, 3, 15]) == 13
    assert solution.maximumDifference([9, 8, 7, 6]) == -1
    assert solution.maximumDifference([1, 2]) == 1
    assert solution.maximumDifference([2, 1]) == -1
    assert solution.maximumDifference(
        [999, 997, 980, 976, 948, 940, 938, 928, 924, 917, 907, 907, 881, 878, 864, 862, 859, 857, 848, 840, 824, 824,
         824, 805, 802, 798, 788, 777, 775, 766, 755, 748, 735, 732, 727, 705, 700, 697, 693, 679, 676, 644, 634, 624,
         599, 596, 588, 583, 562, 558, 553, 539, 537, 536, 509, 491, 485, 483, 454, 449, 438, 425, 403, 368, 345, 327,
         287, 285, 270, 263, 255, 248, 235, 234, 224, 221, 201, 189, 187, 183, 179, 168, 155, 153, 150, 144, 107, 102,
         102, 87, 80, 57, 55, 49, 48, 45, 26, 26, 23, 15]) == -1
