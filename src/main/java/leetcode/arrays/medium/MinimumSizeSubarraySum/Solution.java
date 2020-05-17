package leetcode.arrays.medium.MinimumSizeSubarraySum;


import java.util.Arrays;

/*
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:
Given:
s = 7, nums = [2,3,1,2,4,3]
Result:
2
Explanation:
the subarray [4,3] has the minimal length under the problem constraint.
 */
public class Solution {

    public int minSubArrayLen(int s, int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        Arrays.sort(nums);
        return getSubArrayLen(s, nums);
    }

    private int getSubArrayLen(int s, int[] nums) {
        int sum = 0;
        for (int i = nums.length - 1; i >= 0; i--) {
            sum += nums[i];
            if (sum >= s) {
                return nums.length - i;
            }
        }
        return 0;
    }
}
