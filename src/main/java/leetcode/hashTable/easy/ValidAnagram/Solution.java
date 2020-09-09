package leetcode.hashTable.easy.ValidAnagram;


/*
Given two strings s and t , write a function to determine if t is an anagram of s.

Example:
Given: s = "anagram", t = "nagaram"
Result: true
*/
class Solution {
    public boolean isAnagram(String s, String t) {
        int start = 'a';
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();
        int[] count = new int[26];
        for (int i = 0; i < s.length(); ++i) {
            ++count[sChars[i] - start];
            --count[tChars[i] - start];
        }
        for (int c : count) {
            if (c != 0) {
                return false;
            }
        }
        return true;
    }
}
