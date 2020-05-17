package leetcode.strings.easy.JewelsAndStones;


/*
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
so "a" is considered a different type of stone from "A".

Example:

Given:
J = "aA", S = "aAAbbbb"
Result: 3
*/
public class Solution {

    public int numJewelsInStones(String J, String S) {
        int numOfStones = 0;
        if (J == null || S == null) {
            return 0;
        }
        for (int i = 0; i < S.length(); i++) {
            if (isJewel(J, S.charAt(i))) {
                numOfStones++;
            }
        }
        return numOfStones;
    }

    private boolean isJewel(String J, char charAt) {
        for (int i = 0; i < J.length(); i++) {
            if (J.charAt(i) == charAt) {
                return true;
            }
        }
        return false;
    }
}
