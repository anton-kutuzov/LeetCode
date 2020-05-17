package leetcode.strings.easy.JewelsAndStones;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String J = "aA";
        String S = "aAAbbbb";
        System.out.println(solution.numJewelsInStones(J, S));
    }
}
