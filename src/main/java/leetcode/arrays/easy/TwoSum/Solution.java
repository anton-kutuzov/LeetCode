package leetcode.arrays.easy.TwoSum;


import java.util.HashMap;
import java.util.Map;

/*
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given:
  nums = [2, 7, 11, 15], target = 9

Result:
  nums[0] + nums[1] = 2 + 7 = 9,
  return [0, 1].
*/
public class Solution {

    public int[] twoSum(int[] nums, int target) {
        return twoSumWithMap(nums, target);
    }

    private int[] twoSumWithMap(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int dif = target - nums[i];
            if (map.containsKey(nums[i])) {
                return new int[]{map.get(nums[i]), i};
            }
            map.put(dif, i);
        }
        return new int[]{};
    }

    private int[] twoSumWithMergeSort(int[] nums, int target) {
        int[] indexes = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            indexes[i] = i;
        }
        mergeSort(nums, 0, nums.length - 1, indexes);
        int i = 0, j = nums.length - 1;
        while (i < j) {
            int sum = nums[indexes[i]] + nums[indexes[j]];
            if (sum == target) {
                if (indexes[i] < indexes[j]) {
                    return new int[]{indexes[i], indexes[j]};
                } else {
                    return new int[]{indexes[j], indexes[i]};
                }
            } else if (sum < target) {
                i++;
            } else {
                j--;
            }
        }
        return new int[]{};
    }

    private void mergeSort(int[] array, int start, int end, int[] indexes) {
        if (start >= end) {
            return;
        }
        int mid = (start + end) / 2;
        mergeSort(array, start, mid, indexes);
        mergeSort(array, mid + 1, end, indexes);
        merge(array, start, mid, end, indexes);
    }

    private void merge(int[] a, int start, int mid, int end, int[] indexes) {
        int[] tmp = new int[end - start + 1];
        int pos1 = start;
        int pos2 = mid + 1;
        int pos3 = 0;
        while (pos1 <= mid && pos2 <= end) {
            if (a[indexes[pos1]] < a[indexes[pos2]]) {
                tmp[pos3++] = indexes[pos1++];
            } else {
                tmp[pos3++] = indexes[pos2++];
            }
        }
        while (pos1 <= mid) {
            tmp[pos3++] = indexes[pos1++];
        }
        while (pos2 <= end) {
            tmp[pos3++] = indexes[pos2++];
        }
        System.arraycopy(tmp, 0, indexes, start, end - start + 1);
    }
}
