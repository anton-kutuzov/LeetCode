package leetcode.arrays.easy.RotateArray;


/*
Given an array, rotate the array to the right by k steps, where k is non-negative.
Follow up:
    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?

Example:
Given:
nums = [1,2,3,4,5,6,7], k = 3
Result:
[5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Solution:
1. First of all we reverse full array: [1,2,3,4,5,6,7] --> [7,6,5,4,3,2,1]
2. Then take first k(for example k = 3) elements and revers again: [7,6,5,4,3,2,1] --> [5,6,7,4,3,2,1]
3. Then take elements from k(for example k = 3) to end and revers too: [5,6,7,4,3,2,1] --> [5,6,7,1,2,3,4]
*/
public class Solution {

    public void rotate(int[] nums, int k) {
        if (nums.length < k) {
            return;
        }
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
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
