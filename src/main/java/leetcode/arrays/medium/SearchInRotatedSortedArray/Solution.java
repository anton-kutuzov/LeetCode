package leetcode.arrays.medium.SearchInRotatedSortedArray;


/*
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example:
Given:
nums = [4,5,6,7,0,1,2], target = 0
Result: 4
 */
public class Solution {

    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[start] == target) {
                return start;
            }
            if (nums[end] == target) {
                return end;
            }
            if (nums[mid] < nums[start]) {
                if (target < nums[mid] || target >= nums[start]) {
                    end = mid;
                } else {
                    start = mid + 1;
                }
            } else {
                if (target < nums[mid] && target >= nums[start]) {
                    end = mid;
                } else {
                    start = mid + 1;
                }
            }
        }
        return -1;
    }
}
