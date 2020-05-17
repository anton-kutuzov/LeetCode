package leetcode.bitManipulations.easy.HammingDistance;


/*
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note:
0 ≤ x, y < 231.

Example:
Given:
x = 1, y = 4
Result:
2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
*/
public class Solution {
    public int hammingDistance(int x, int y) {
        return bitCount(x ^ y);
    }

    private int bitCount(int x) {
        int count = 0;
        while (x != 0) {
            count += x & 1;
            x = x >> 1;
        }
        return count;
    }
}
