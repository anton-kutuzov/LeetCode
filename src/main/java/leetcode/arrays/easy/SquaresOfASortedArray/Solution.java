package leetcode.arrays.easy.SquaresOfASortedArray;


/*
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example:
Given:
[-4,-1,0,3,10]
Result:
[0,1,9,16,100]
*/
public class Solution {

    public int[] sortedSquares(int[] A) {
        int[] b = new int[A.length];
        int i = 0;
        int j = A.length - 1;
        int k = A.length - 1;
        while(i <= j) {
            if (A[i] * A[i] > A[j] * A[j]) {
                b[k--] = A[i] * A[i];
                i++;
            } else {
                b[k--] = A[j] * A[j];
                j--;
            }
        }
        return b;
    }
}
