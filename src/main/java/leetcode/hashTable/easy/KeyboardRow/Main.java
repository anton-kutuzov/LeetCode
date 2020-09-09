package leetcode.hashTable.easy.KeyboardRow;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String[] str1 = {"Hello", "Alaska", "Dad", "Peace"};
        String[] str2 = {"Hello", "Alaska", "", "Peace"};
        String[] str3 = {};
        String[] str4 = {"Dad"};
        System.out.println(Arrays.toString(solution.findWords(str1)));
        System.out.println(Arrays.toString(solution.findWords(str2)));
        System.out.println(Arrays.toString(solution.findWords(str3)));
        System.out.println(Arrays.toString(solution.findWords(str4)));
    }
}
