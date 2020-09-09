package leetcode.greedy.medium.SplitArrayIntoFibonacciSequence;


import java.util.ArrayList;
import java.util.List;

/*
Given a string S of digits, such as S = "123456579", we can split it longo a Fibonacci-like sequence [123, 456, 579].
Formally, a Fibonacci-like sequence is a list F of non-negative Longs such that:
    0 <= F[i] <= 2^31 - 1, (that is, each Long fits a 32-bit signed Long type);
    F.length >= 3;
    and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string longo pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.
Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example:
Given:
"123456579"
Result:
[123,456,579]
*/
public class Solution {
    final static int[] sizeTable = {9, 99, 999, 9999, 99999, 999999, 9999999,
            99999999, 999999999, Integer.MAX_VALUE};

    public List<Integer> splitIntoFibonacci(String s) {
        List<Integer> result = new ArrayList<>();
        int num = 0;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(0) == '0' && i > 1) {
                continue;
            }
            num = num * 10 + getInt(s.charAt(i - 1));
            boolean found = false;
            int length = 0;
            int num2 = 0;
            for (int j = 1; ; j++) {
                if (s.charAt(i) == '0' && j > 1) {
                    break;
                }
                num2 = num2 * 10 + getInt(s.charAt(i + j - 1));
                int res = num + num2;
                length = i + j + intSize(res);
                if (length > s.length()) {
                    break;
                }
                String num3S = s.substring(i + j, length);
                long num3 = Long.parseLong(num3S);
                if (num3 >= Integer.MAX_VALUE) {
                    break;
                }
                if (isNotCorrectInt(num3S)) {
                    continue;
                }
                if (num3 == res) {
                    result.add(num);
                    result.add(num2);
                    result.add((int) num3);
                    found = true;
                    break;
                }
            }
            while (found) {
                int res = result.get(result.size() - 1) + result.get(result.size() - 2);
                int endIndex = length + String.valueOf(res).length();
                if (endIndex > s.length()) {
                    break;
                }
                String substring = s.substring(length, endIndex);
                long num3 = Long.parseLong(substring);
                if (isNotCorrectInt(substring) || num3 >= Integer.MAX_VALUE) {
                    result = new ArrayList<>();
                    found = false;
                    break;
                }
                if (num3 != res) {
                    result = new ArrayList<>();
                    found = false;
                    break;
                }
                result.add((int) num3);
                length += substring.length();
            }
            if (found && length >= s.length()) {
                return result;
            }
        }
        return new ArrayList<>();


    }

    private int getInt(char c) {
        switch (c) {
            case '0':
                return 0;
            case '1':
                return 1;
            case '2':
                return 2;
            case '3':
                return 3;
            case '4':
                return 4;
            case '5':
                return 5;
            case '6':
                return 6;
            case '7':
                return 7;
            case '8':
                return 8;
            case '9':
                return 9;
        }
        return 0;
    }

    static int intSize(int x) {
        for (int i = 0; ; i++) {
            if (x <= sizeTable[i]) {
                return i + 1;
            }
        }
    }

    private boolean isNotCorrectInt(String s) {
        return (s.charAt(0) == '0' && s.length() > 1);
    }
}
