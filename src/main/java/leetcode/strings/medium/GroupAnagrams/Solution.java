package leetcode.strings.medium.GroupAnagrams;


import java.util.*;

/*
Given an array of strings, group anagrams together.

Example:

Given:
["eat", "tea", "tan", "ate", "nat", "bat"],
Result:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
*/
public class Solution {
    private static final int ARRAY_SIZE = 26;

    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<Integer, List<String>> map = new HashMap<>();
        for (String str : strs) {
            map.computeIfAbsent(getHashCode(str), (i) -> new ArrayList<>()).add(str);
        }
        return new ArrayList<>(map.values());
    }

    private int getHashCode(String str) {
        int[] count = new int[ARRAY_SIZE];
        for (char c : str.toCharArray()) {
            count[c - 'a']++;
        }
        return Arrays.hashCode(count);
    }
}
