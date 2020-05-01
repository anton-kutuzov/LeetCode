package leetcode.arrays.medium.FindTheDuplicateNumber;


/*
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example:
Given:
[1,3,4,2,2]
Result:
2
*/
public class Solution {

    public int findDuplicate(int[] nums) {
        int result = 0;
        for (int i = 0; i < nums.length; i++) {
            int ind = Math.abs(nums[i]);
            if (nums[ind] < 0) {
                result = ind;
                break;
            } else {
                nums[ind] = -nums[ind];
            }
        }
        for (int i = 0; i < nums.length; i++) {
            nums[i] = Math.abs(nums[i]);
        }
        return result;
    }


}
