package leetcode.bitManipulations.easy.NumberComplement;


/*
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.
Example:

Given: num = 5
Result: 2
Explanation: The binary representation of 5 is 101, and its complement is 010. So you need to output 2.

Solution:
Reverse each bit and then convert into number
*/
public class Solution {
    public int complement(int num) {
        int pow = 0;
        int result = 0;
        while (num != 0) {
            //(((num & 1) == 1) ? 0 : 1) - reverse the bit
            //x << pow++ it's mean x * 2^pow
            result += (((num & 1) == 1) ? 0 : 1) << pow++;
            num = num >> 1;
        }
        return result;
    }

}
