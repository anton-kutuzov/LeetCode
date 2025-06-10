package leetcode.arrays.easy.MissingNumber;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {9, 6, 4, 2, 3, 5, 7, 0, 1};
        int[] nums2 = {0, 1};
        int[] nums3 = {0};
        int[] nums4 = {1};
        int[] nums5 = {};
        int[] nums6 = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        int[] nums7 = {0, 1, 2, 3, 4, 5, 6, 7, 8};
        int[] nums8 = {0, 1, 2, 3, 9, 5, 6, 7, 8};
        System.out.println(solution.missingNumber(nums) + " = 8");
        System.out.println(solution.missingNumber(nums2) + " = 2");
        System.out.println(solution.missingNumber(nums3) + " = 1");
        System.out.println(solution.missingNumber(nums4) + " = 0");
        System.out.println(solution.missingNumber(nums5) + " = 0");
        System.out.println(solution.missingNumber(nums6) + " = 0");
        System.out.println(solution.missingNumber(nums7) + " = 9");
        System.out.println(solution.missingNumber(nums8) + " = 4");
    }
}
