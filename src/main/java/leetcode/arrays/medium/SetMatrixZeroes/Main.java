package leetcode.arrays.medium.SetMatrixZeroes;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] array = {
            new int[]{1, 1, 1},
            new int[]{0, 1, 2}
        };
        solution.setZeroes(array);
        for (int[] ints : array) {
            System.out.println(Arrays.toString(ints));
        }
    }

}
