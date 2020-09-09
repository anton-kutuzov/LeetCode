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
        if (nums.length == 1) {
            return nums[0] >= s ? 1 : 0;
        }
        return getSubArrayLen(s, nums);
    }

    private int getSubArrayLen(int s, int[] nums) {
        int sum = nums[0];
        int i = 0;
        int j = 0;
        int min = Integer.MAX_VALUE;
        while (i <= j && j < nums.length - 1) {
            while (sum < s && j < nums.length - 1) {
                sum += nums[++j];
            }
            while (sum >= s && i <= j) {
                if (min > j - i + 1) {
                    min = (j - i + 1);
                }
                sum -= nums[i++];
            }
        }
        return min == Integer.MAX_VALUE ? 0 : min;
    }
}
