package leetcode.strings.easy.RobotReturnToOrigin;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String str1 = "UD";
        String str2 = "LL";
        String str3 = "URULDLDR";
        String str4 = "UUDDLLRR";
        String str5 = "";
        System.out.println(solution.judgeCircle(str1));
        System.out.println(solution.judgeCircle(str2));
        System.out.println(solution.judgeCircle(str3));
        System.out.println(solution.judgeCircle(str4));
        System.out.println(solution.judgeCircle(str5));
    }
}
