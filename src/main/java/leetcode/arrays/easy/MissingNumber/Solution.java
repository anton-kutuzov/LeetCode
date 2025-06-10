package leetcode.arrays.easy.MissingNumber;


/*
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example:
Given: [3,0,1]
Result: 2

Solution 1
We use value of array as index in this array and mark elements of array as negative and add 1(it's need because we have zero)
In the end all index of all positive elements of array it's not exist numbers
Solution 2
We can harness the fact that XOR is its own inverse to find the missing element in linear time.
Solution 3
Gauss' Formula
Sum from 0 to n equals n*(n+1)/2
*/
class Solution {
    public int missingNumber(int[] nums) { //Solution 2
        int result = nums.length;
        for (int i = 0; i < nums.length; i++) {
            result ^= i ^ nums[i];
        }
        return result;
    }

    public int missingNumber2(int[] nums) { //Solution 3
        int expectedSum = nums.length * (nums.length + 1) / 2;
        int actualSum = 0;
        for (int num : nums) {
            actualSum += num;
        }
        return expectedSum - actualSum;
    }

    public int missingNumber1(int[] nums) { //Solution 1
        for (int i = 0; i < nums.length; i++) {
            int index = 0;
            if (nums[i] >= 0) {
                index = nums[i];
            } else if (nums[i] < 0) {
                index = -(nums[i] + 1);
            }
            if (index < nums.length) {
                nums[index] = -Math.abs(nums[index]) - 1;
            }
        }
        int i = 0;
        while (i < nums.length) {
            if (nums[i] >= 0) {
                return i;
            }
            i++;
        }
        return i;
    }
}
