package leetcode.bitManipulations.medium.CountingBits;


/*
Given a non negative integer number num.
For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:

Given: 5
Result: [0,1,1,2,1,2]

Follow up:
    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
*/
public class Solution {

    public int[] countBits(int i) {
        int[] counts = new int[i + 1];
        for (int num = 1; num <= i; num++) {
            counts[num] = counts[num / 2] + (num & 1);
        }
        return counts;
    }

    public int[] countBits2(int i) {
        int[] counts = new int[i + 1];
        for (int num = 1; num <= i; num++) {
            int count = 0;
            int current = num;
            while (current > 0) {
                System.out.print((current & 1) + " ");
                count += current & 1;
                current = current >> 1;
            }
            counts[num] = count;
            System.out.println();
            System.out.println("---- " + (num ^ num - 1));
        }
        return counts;
    }
}
