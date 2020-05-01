package leetcode.arrays.easy.MergeSortedArray;


/*
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:
Given:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Result
[1,2,2,3,5,6]

*/
public class Solution {

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int pos1 = 0;
        int pos2 = 0;
        int pos3 = 0;
        int[] b = new int[nums1.length];
        while (pos1 < m && pos2 < n) {
            if (nums1[pos1] < nums2[pos2]) {
                b[pos3++] = nums1[pos1++];
            } else {
                b[pos3++] = nums2[pos2++];
            }
        }
        while (pos1 < m) {
            b[pos3++] = nums1[pos1++];
        }
        while (pos2 < n) {
            b[pos3++] = nums2[pos2++];
        }
        System.arraycopy(b, 0, nums1, 0, nums1.length);
    }
}
