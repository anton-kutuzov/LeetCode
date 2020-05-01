package leetcode.arrays.medium.FindPeakElement;


/*
A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] != nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Example:
Given:
nums = [1,2,3,1]
Result:
2
Explanation: 3 is a peak element and your function should return the index number 2.
*/
public class Solution {

    public int findPeakElement(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        while (l < r) {
            int mid = (l + r) / 2;
            if (nums[mid] > nums[mid + 1]) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return r;
    }
}
