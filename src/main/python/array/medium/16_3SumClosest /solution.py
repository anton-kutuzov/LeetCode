from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res_sum = sum(nums[:3])
        len_nums = len(nums)
        for i in range(len_nums - 2):

            left, right = i + 1, len_nums - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if abs(res_sum - target) > abs(cur_sum - target):
                    res_sum = cur_sum
                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    return res_sum
        return res_sum

    def threeSumClosestBruteForce(self, nums: List[int], target: int) -> int:
        min_diff = None
        res_sum = 0
        len_nums = len(nums)
        for i in range(len_nums - 2):
            for j in range(i + 1, len_nums):
                if i == j:
                    continue
                for k in range(j + 1, len_nums):
                    if i == k or k == j:
                        continue
                    cur_sum = nums[i] + nums[j] + nums[k]
                    if min_diff is None or min_diff > abs(cur_sum - target):
                        min_diff = abs(cur_sum - target)
                        res_sum = cur_sum

        return 0 if res_sum is None else res_sum


if __name__ == '__main__':
    solution = Solution()
    assert solution.threeSumClosestBruteForce([-1, 2, 1, -4], 1) == 2
    assert solution.threeSumClosestBruteForce([0, 0, 0], 1) == 0
    assert solution.threeSumClosestBruteForce([8, -7, 0, 2, 2], 1) == 1

    assert solution.threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert solution.threeSumClosest([0, 0, 0], 1) == 0
    assert solution.threeSumClosest([8, -7, 0, 2, 2], 1) == 1
    assert solution.threeSumClosest(
        [-314, 975, -143, 23, 897, 714, 956, 654, 690, -345, -989, -979, -826, -299, -408, 933, 588, -619, -491, -99,
         -353, -182, 411, 978, -261, -271, -983, -60, -874, 11, 253, -198, 977, 99, 371, -884, 14, -482, -757, 251, 869,
         587, -706, -885, -220, -472, 738, 996, 22, 923, 407, 926, -759, 851, -124, 513, -142, 60, 268, -944, 612, 890,
         192, 964, 34, -368, 910, 651, 18, 152, -239, 900, 991, 646, 559, -668, 246, 256, 111, 375, 195, 197, -935,
         -457, -371, -251, 968, 162, 515, 473, 438, -349, -347, -116, -31, -579, 145, 183, -602, -128, 421, -815, -824,
         650, -170, 285, 708, -268, -105, 166, -914, 325, 368, -429, 405, -42, 349, -570, 228, -702, -875, 773, -304,
         -865, -323, -215, 364, -910, 671, -937, -356, 734, -844, -506, 682, 46, 648, 76, 477, -996, -419, 603, -134,
         -504, 328, 331, 494, -293, -978, 931, -68, 401, -37, 3, -410, -362, 698, 535, 135, 279, 959, -65, -374, -916,
         -375, -746, -565, 642, 378, 275, 21, -597, 259, -62, -463, -434, -707, -49, -859, 462, 394, -227, 70, 239,
         -450, 707, -36, -762, -540, 985, 417, 821, -69, -561, 63, 637, -384, -691, -361, 223, -127, 122, -318, 564,
         128, -195, 217, 102, -742, 597, 220, -240, -711, 323, -342, -138, -678, -648, 954, -918, 153, -77, 388, -854,
         -804, 873, 823, 557, -840, 106, -675, -201, -873, 73, -67, -275, 620, -735, -93, -91, 350, -322, -806, 213,
         -674, -10, -102, 655, 713, -572, -933, 563, -58, 881, 110, -527, 731, -987, 376, -451, -163, -718, -513, -175,
         495, -183, -629, 550, 945, -659, -601, 854, -562, 413, 842, 470, 706, 489, -38, 863, -535, 48, -564, 158, -468,
         806, 922, -667, -12, 579, -743, -582, -909, 117, 437, -763, -174, 683, 131, -233, -587, 62, -259, -319, 294,
         -237, -591, -770, -141, -656, 283, -213, -494, -439, -796, 750, -890, -799, -850, 454, -34, -159, -787, 43,
         493, -794, -972, 383], 9486) == 2972