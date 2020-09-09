package leetcode.arrays.easy.ArrayPartitionI;


/*
 Given an array of 2n integers, your task is to group these integers into n pairs of integer,
 say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example:
Given: [1,4,3,2]
Result: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
    n is a positive integer, which is in the range of [1, 10000].
    All the integers in the array will be in the range of [-10000, 10000].

Solution:
1. Sort array. In this case we can use countableSort.
2. Calculate sum of elements with index equals 'i % 2 == 0'
*/
class Solution {
    public int arrayPairSum(int[] nums) {
        int[] tmp = new int[20001];
        for (int num : nums) {
            ++tmp[num + 10000];
        }
        for (int i = 1; i < tmp.length; ++i) {
            tmp[i] += tmp[i - 1];
        }
        int sum = 0;
        for (int num : nums) {
            //a & 1 == 0 it's same as a % 2 == 0
            if ((((--tmp[num + 10000])) & 1) == 0) {
                sum += num;
            }
        }
        return sum;
    }
}
