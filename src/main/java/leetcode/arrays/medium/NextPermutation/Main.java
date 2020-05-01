package leetcode.arrays.medium.NextPermutation;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        //int[] array = {5,4,2,1};
        //int[] array = {1,0,2,1};
        //int[] array = {2,4,2,1,5,1};
        int[] array = {1, 3, 2};
        solution.nextPermutation(array);
        System.out.println(Arrays.toString(array));
    }
}
