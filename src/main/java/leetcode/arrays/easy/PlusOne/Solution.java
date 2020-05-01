package leetcode.arrays.easy.PlusOne;


/*
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example:
Given:
[1,2,3,4,5,6,7] and k = 3
Result:
[5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

*/
public class Solution {

    public int[] plusOne(int[] digits) {
        int i = digits.length - 1;
        while (i >= 0 && digits[i] + 1 > 9) {
            digits[i] = 0;
            i--;
        }
        if (i < 0) {
            int[] b = new int[digits.length + 1];
            b[0] = 1;
            return b;
        } else {
            digits[i] += 1;
            return digits;
        }
    }
}
