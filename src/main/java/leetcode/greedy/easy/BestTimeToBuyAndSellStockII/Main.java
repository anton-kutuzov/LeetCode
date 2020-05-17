package leetcode.greedy.easy.BestTimeToBuyAndSellStockII;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        //int[] array = {7,1,5,3,6,7};
        //int[] array = {0,0,0,0,0,0};
        //int[] array = {3,3,3,3,3,3};
        int[] array = {1, 2, 3, 4, 5, 1};
        System.out.println(solution.maxProfit((array)));
    }
}
