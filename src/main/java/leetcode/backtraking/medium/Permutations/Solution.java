package leetcode.backtraking.medium.Permutations;

import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;

/*
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

*/
public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        permute(list, new LinkedHashSet<>(), nums);
        return list;
    }

    private void permute(List<List<Integer>> list, Set<Integer> cur, int[] nums) {
        if (cur.size() >= nums.length) {
            list.add(new ArrayList<>(cur));
            return;
        }
        for (int num : nums) {
            if (cur.contains(num)) {
                continue;
            }
            cur.add(num);
            permute(list, cur, nums);
            cur.remove(num);
        }
    }
}
