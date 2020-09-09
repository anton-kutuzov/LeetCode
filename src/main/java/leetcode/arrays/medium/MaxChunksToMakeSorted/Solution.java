package leetcode.arrays.medium.MaxChunksToMakeSorted;


/*
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.
After concatenating them, the result equals the sorted array.
What is the most number of chunks we could have made?

Example:
Given:
arr = [1,0,2,3,4]
Result:
4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
Note:
    arr will have length in range [1, 10].
    arr[i] will be a permutation of [0, 1, ..., arr.length - 1].
*/
public class Solution {
    public int maxChunksToSorted(int[] arr) {
        int numOfChunks = 0;
        int max = 0;
        for (int i = 0; i < arr.length; i++) {
            if (max < arr[i]) {
                max = arr[i];
            }
            if (max == i) {
                numOfChunks++;
            }
        }
        return numOfChunks;
    }
}
