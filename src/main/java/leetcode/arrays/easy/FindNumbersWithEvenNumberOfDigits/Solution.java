package leetcode.arrays.easy.FindNumbersWithEvenNumberOfDigits;


/*
Given an array nums of integers, return how many of them contain an even number of digits.

Example:
Given:
nums = [12,345,2,6,7896]
Result:
2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.
*/
public class Solution {

    public int findNumbers(int[] nums) {
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            if (isEven(getNumberOfDigits(nums[i]))) {
                res++;
            }
        }
        return res++;
    }

    private int getNumberOfDigits(int n) {
        int i = 0;
        while (n > 0) {
            n = n / 10;
            i++;
        }
        return i;
    }

    private boolean isEven(int n) {
        return n % 2 == 0;
    }
}
