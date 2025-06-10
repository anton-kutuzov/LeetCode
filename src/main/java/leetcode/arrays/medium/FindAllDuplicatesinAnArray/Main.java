package leetcode.arrays.medium.FindAllDuplicatesinAnArray;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] array = {4, 3, 2, 7, 8, 2, 3, 1};
        int[] array2 = {1, 2, 3, 5, 8, 7, 2, 1};
        System.out.println(solution.findDuplicates((array)));
        System.out.println(solution.findDuplicates((array2)));
    }
}
