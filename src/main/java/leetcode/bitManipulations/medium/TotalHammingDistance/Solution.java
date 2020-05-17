package leetcode.bitManipulations.medium.TotalHammingDistance;


/*
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Given:
4, 14, 2
Result:
6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
*/
public class Solution {
    //This is slow implementation 32*n ~ O(n)
    public int totalHammingDistance(int[] nums) {
        int totalCount = 0;
        for (int i = 0; i < 32; i++) {
            int count = 0;
            for (int j = 0; j < nums.length; j++) {
                count += nums[j] & 1;
                nums[j] = nums[j] >> 1;
            }
            totalCount += count * (nums.length - count);
        }
        return totalCount;
    }

    //This is slow implementation O(n*n)
    public int totalHammingDistance2(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                count += hammingDistance(nums[i], nums[j]);
            }
        }
        return count;
    }

    private static int hammingDistance(int x, int y) {
        int count = 0;
        int xor = x ^ y;
        while (xor != 0) {
            count += xor & 1;
            xor = xor >> 1;
        }
        return count;
    }
}
