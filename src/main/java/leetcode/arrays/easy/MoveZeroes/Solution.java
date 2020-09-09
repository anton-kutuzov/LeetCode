package leetcode.arrays.easy.MoveZeroes;


/*
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Given:
[0,1,0,3,12]
Result:
[1,3,12,0,0]

Solution:
We use two pointer 'i' and 'j'. We iterate by array and if we find non-zero number we write it on position 'j' and increase j.
*/
public class Solution {

    public void moveZeroes(int[] nums) {
        int j = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[j++] = nums[i];
            }
        }
        for (int i = j; i < nums.length; i++) {
            nums[i] = 0;
        }
    }
}
