package leetcode.arrays.easy.ArrayPartitionI;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] array1 = {1, 3, 4, 2};
        int[] array2 = {-10000, 4, 3, 2, 5, 6, 8, 10, 3, 6, 4, 5};
        System.out.println(solution.arrayPairSum(array1) + " == 4");
        System.out.println(solution.arrayPairSum(array2) + " == -9974");
    }
}
