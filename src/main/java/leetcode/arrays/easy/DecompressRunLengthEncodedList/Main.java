package leetcode.arrays.easy.DecompressRunLengthEncodedList;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] array = {5, 3, 1, 2};
        System.out.println(Arrays.toString(solution.decompressRLElist(array)));
    }
}
