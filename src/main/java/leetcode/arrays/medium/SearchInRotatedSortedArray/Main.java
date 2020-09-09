package leetcode.arrays.medium.SearchInRotatedSortedArray;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        //int[] array = {4,5,6,7,0,1,2};
        int[] array = {5, 1, 2, 3, 4};
        //int[] array = {8,9,2,3,4};
        System.out.println(solution.search(array, 9));
        System.out.println(solution.search(array, 8));
        System.out.println(solution.search(array, 4));
        System.out.println(solution.search(array, 5));
        System.out.println(solution.search(array, 6));
        System.out.println(solution.search(array, 7));
        System.out.println(solution.search(array, 0));
        System.out.println(solution.search(array, 1));
        System.out.println(solution.search(array, 2));
        System.out.println(solution.search(array, 3));
    }

}
