package leetcode.greedy.medium.SplitArrayIntoFibonacciSequence;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String str = "123456579";
        String str2 = "112358130";
        String str3 = "0123";
        String str4 = "1101111";
        String str5 = "11235813";
        String str6 = "112";
        String str7 = "111121325";
        String str8 = "000000000";
        String str9 = "101";
        String str10 = "214748364721474836422147483641";
        String str11 = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511";
        String str12 = "2820022842865610841740282445647388119521934031292";
        System.out.println(solution.splitIntoFibonacci(str12) + " --> [28,200,228,428,656,1084,1740,2824,4564,7388,11952,19340,31292]");
        System.out.println(solution.splitIntoFibonacci(str) + " --> [123, 456, 579]");
        System.out.println(solution.splitIntoFibonacci(str2) + " --> []");
        System.out.println(solution.splitIntoFibonacci(str3) + " --> []");
        System.out.println(solution.splitIntoFibonacci(str4) + " --> [11, 0, 11, 11]");
        System.out.println(solution.splitIntoFibonacci(str5) + " --> [1, 1, 2, 3, 5, 8, 13]");
        System.out.println(solution.splitIntoFibonacci(str6) + " --> [1, 1, 2]");
        System.out.println(solution.splitIntoFibonacci(str7) + " --> [11, 1, 12, 13, 25]");
        System.out.println(solution.splitIntoFibonacci(str8) + " --> [0, 0, 0, 0, 0, 0, 0, 0, 0]");
        System.out.println(solution.splitIntoFibonacci(str9) + " --> [1, 0, 1]");
        System.out.println(solution.splitIntoFibonacci(str10) + " --> []");
        System.out.println(solution.splitIntoFibonacci(str11) + " --> []");
    }
}
