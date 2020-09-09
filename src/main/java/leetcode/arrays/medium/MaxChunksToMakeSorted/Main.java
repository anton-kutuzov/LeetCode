package leetcode.arrays.medium.MaxChunksToMakeSorted;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] array1 = {0, 2, 1, 4, 3};
        int[] array2 = {0, 2, 3, 1, 4};
        int[] array3 = {4, 3, 2, 1, 0};
        int[] array4 = {4, 3, 1, 2, 0};
        int[] array5 = {0, 1, 2, 3, 4};
        int[] array6 = {0, 4, 5, 2, 1, 3};
        System.out.println(solution.maxChunksToSorted(array1) + " --> " + "3");
        System.out.println(solution.maxChunksToSorted(array2) + " --> " + "3");
        System.out.println(solution.maxChunksToSorted(array3) + " --> " + "1");
        System.out.println(solution.maxChunksToSorted(array4) + " --> " + "1");
        System.out.println(solution.maxChunksToSorted(array5) + " --> " + "5");
        System.out.println(solution.maxChunksToSorted(array6) + " --> " + "2");
    }
}
