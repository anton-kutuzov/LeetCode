package leetcode.stack.easy.RemoveOutermostParentheses;


import java.util.*;

/*
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings,
and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

Example:
Given:
"(()())(())(()(()))"
Result:
"()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
*/
public class Solution {

    public String removeOuterParentheses(String s) {
        StringBuilder output = new StringBuilder();
        int stackSize = 0;
        for (int i = 0; i < s.length(); i++) {
            char currentParenthesis = s.charAt(i);
            if (!(stackSize == 1 && currentParenthesis == ')') &&
                    !(stackSize == 0 && currentParenthesis == '(')) {
                output.append(currentParenthesis);
            }
            if (currentParenthesis == '(') {
                stackSize++;
            } else {
                stackSize--;
            }
        }
        return output.toString();
    }
}
