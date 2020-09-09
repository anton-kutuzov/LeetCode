package leetcode.strings.medium.GenerateParentheses;


import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/*
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example,
Given n = 3

Result: set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
*/
public class Solution {

    public List<String> generateParenthesis(int n) {
        LinkedList<String> list = new LinkedList<>();
        generateParenthesis(list, 0, 0, "", n);
        return list;
    }

    private void generateParenthesis(List<String> list, int open, int close, String s, int n) {
        if (open >= n && close >= n) {
            list.add(s);
            return;
        }
        if (open < n) {
            generateParenthesis(list, open + 1, close, s + "(", n);
        }
        if (close < open) {
            generateParenthesis(list, open, close + 1, s + ")", n);
        }
    }
}
