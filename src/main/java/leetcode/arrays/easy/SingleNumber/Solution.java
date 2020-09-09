package leetcode.arrays.easy.SingleNumber;


import java.util.HashMap;
import java.util.Map;

/*
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example:
Given:
[2,2,1]
Result:
1

Solution:
1. Use map. Key is digital, value is count.
2. Find first digital with count 1.
*/
public class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>(nums.length);
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i]) + 1);
            } else {
                map.put(nums[i], 1);
            }
        }
        return map.entrySet().stream().filter(e -> e.getValue() != 2).map(Map.Entry::getKey).findFirst().orElse(0);
    }
}
