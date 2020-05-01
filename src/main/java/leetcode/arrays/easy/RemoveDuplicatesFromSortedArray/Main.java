package leetcode.arrays.easy.RemoveDuplicatesFromSortedArray;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] array = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        //int[] array = {1, 2, 2};
        //int[] array = {1, 1, 2};
        //int[] array = {2, 2, 2};
        //int[] array = {1, 2, 3};
        //int[] array = {-3,-3,-2,-1,-1,0,0,0,0,0};
        System.out.println(solution.removeDuplicates(array));
        System.out.println(Arrays.toString(array));
    }
}
