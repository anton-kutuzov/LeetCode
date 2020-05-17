package leetcode.stack.easy.RemoveOutermostParentheses;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = "()(()())(())(()((())))()";
        System.out.println(solution.removeOuterParentheses(s));
    }
}
