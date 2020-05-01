package leetcode.arrays.medium.RotateImage;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] array = {new int[]{1, 3, 2},
            new int[]{1, 5, 8},
            new int[]{6, 15, 90}};
        solution.rotate(array);
        for (int[] ints : array) {
            System.out.println(Arrays.toString(ints));
        }
    }

}
