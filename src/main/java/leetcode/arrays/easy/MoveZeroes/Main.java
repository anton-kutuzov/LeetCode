package leetcode.arrays.easy.MoveZeroes;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] array = {0, 0, 0, 1, 0, 5};
        solution.moveZeroes(array);
        System.out.println(Arrays.toString(array));
    }
}
