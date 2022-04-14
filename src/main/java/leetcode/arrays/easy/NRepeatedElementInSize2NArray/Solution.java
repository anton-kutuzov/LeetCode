package leetcode.arrays.easy.NRepeatedElementInSize2NArray;


/*
You are given an integer array nums with the following properties:

    nums.length == 2 * n.
    nums contains n + 1 unique elements.
    Exactly one element of nums is repeated n times.

Return the element that is repeated n times.

Input: nums = [2,1,2,5,3,2]
Output: 2
*/
public class Solution {

    public int repeatedNTimes(int[] nums) {
        boolean[] tmp = new boolean[10000];
        for (int num : nums) {
            if (tmp[num]) {
                return num;
            }
            tmp[num] = true;
        }
        return 0;
    }
}
