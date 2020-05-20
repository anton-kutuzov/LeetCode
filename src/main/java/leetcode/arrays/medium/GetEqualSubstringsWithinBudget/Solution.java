package leetcode.arrays.medium.GetEqualSubstringsWithinBudget;


/*
You are given two strings s and t of the same length. You want to change s to t.
Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.
You are also given an integer maxCost.
Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of twith a cost less than or equal to maxCost.
If there is no substring from s that can be changed to its corresponding substring from t, return 0.

Example:
Given:
s = "abcd", t = "bcdf", maxCost = 3
Result:
3
Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.
 */
public class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int costs = 0;
        int max = 0;
        int i = 0, j = 0;
        for (; i < s.length(); i++) {
            costs += Math.abs(s.charAt(i) - t.charAt(i));
            if (costs > maxCost) {
                if (max < i - j) {
                    max = i - j;
                }
                while (costs > maxCost && i < s.length() - 1) {
                    costs -= Math.abs(s.charAt(j) - t.charAt(j));
                    j++;
                    i++;
                    costs += Math.abs(s.charAt(i) - t.charAt(i));
                }
            }
        }
        if (costs <= maxCost) {
            if (max < i - j) {
                max = i - j;
            }
        }
        return max;
    }
}
