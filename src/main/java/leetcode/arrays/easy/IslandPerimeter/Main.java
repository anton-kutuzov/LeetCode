package leetcode.arrays.easy.IslandPerimeter;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] grind = {{0, 1, 0, 0}, {1, 1, 1, 0}, {0, 1, 0, 0}, {1, 1, 0, 0}};
        System.out.println(solution.islandPerimeter(grind));//16
    }
}
