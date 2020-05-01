package leetcode.arrays.easy.PlusOne;


import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] array = {0};
        //int[] array = {9, 9};
        //int[] array = {9, 0};
        //int[] array = {2, 7, 0, 0};
        System.out.println(Arrays.toString(solution.plusOne(array)));
    }
}
