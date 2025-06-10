package leetcode.arrays.easy.MaxConsecutiveOnes;


/*
Given a binary array, find the maximum number of consecutive 1s in this array.

Example:
Given:
[1,1,0,1,1,1]
Result:
3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

Solution:
1. If number is zero, then we are zeroize current length
2. If number is one,  then we are add one to length and update max length
*/
public class Solution {

    public int findMaxConsecutiveOnes(int[] nums) {
        int length = 0;
        int maxLength = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                length = 0;
            } else {
                length++;
                if (maxLength < length) {
                    maxLength = length;
                }
            }
        }
        return maxLength;
    }
}
