package leetcode.arrays.medium.NextPermutation;


/*
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.

Example:
Given:
[1,2,3]
Result:
[1,3,2]

Given:
[3,2,1]
Result:
[1,2,3]
*/
public class Solution {

    public void nextPermutation(int[] nums) {
        int i = 0;
        int j = -1;
        for (i = nums.length - 1; i > 0; i--) {
            if (nums[i] > nums[i - 1]) {
                j = i - 1;
                break;
            }
        }
        if (j >= 0) {
            for (i = j + 1; i < nums.length; i++) {
                if (nums[j] >= nums[i]) {
                    swap(nums, j, i - 1);
                    break;
                } else if (i == nums.length - 1) {
                    swap(nums, j, nums.length - 1);
                    break;
                }
            }
            reverse(nums, j + 1, nums.length - 1);
        } else {
            reverse(nums, 0, nums.length - 1);
        }
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            swap(nums, start++, end--);
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
