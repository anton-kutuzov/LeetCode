package leetcode.arrays.easy.PlusOne;


/*
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Given:
digits = [1,2,3]
Result:
[1,2,4]
Explanation:
The array represents the integer 123.

Solution:
1. Iterate from end of array by 1 while the 'number + 1 > 9'
2. If we find element and index > 0 then we add 1 to the number on 'i' position
3. If index < 0 then we allocate new array we size +1 we write first digital as 1
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
