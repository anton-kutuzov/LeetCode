package leetcode.arrays.easy.RemoveElement;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] array = {3, 2, 4};
        System.out.println(solution.removeElement(array, 3));
        System.out.println(Arrays.toString(array));
    }
}
