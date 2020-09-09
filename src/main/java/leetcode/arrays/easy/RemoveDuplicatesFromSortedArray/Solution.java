package leetcode.arrays.easy.RemoveDuplicatesFromSortedArray;

/*
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.

Example:
  Given:
  nums = [1,1,2]

Result:
 Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
 It doesn't matter what you leave beyond the new length.

Solution:
We use two pointers.
When we find not equals elements by indexes 'j' and 'i' we are add one to 'j' and write digital on position 'i' to position 'j'
*/
public class Solution {

    public int removeDuplicates(int[] nums) {
        return secondVersion(nums);
    }

    private int secondVersion(int[] nums) {
        int i = 1;
        int j = 0;
        while (i < nums.length) {
            if (nums[i] != nums[j]) {
                nums[++j] = nums[i];
            }
            i++;
        }
        return j + 1;
    }

    private int firstVersion(int[] nums) {
        int k = 0;
        int i = 0;
        while (i < nums.length) {
            int nextOtherIndex = findIndexOfNextOther(nums, i);
            if (nextOtherIndex != i) {
                nums[k] = nums[nextOtherIndex >= nums.length ? nums.length - 1 : nextOtherIndex];
                i = nextOtherIndex + 1;
                k++;
            } else {
                nums[k++] = nums[i++];
            }
        }
        return k;
    }

    private int findIndexOfNextOther(int[] nums, int start) {
        boolean find = false;
        int i = start + 1;
        int current = nums[start];
        while (i < nums.length && current == nums[i]) {
            i++;
            find = true;
        }
        return find ? i - 1 : start;
    }
}
