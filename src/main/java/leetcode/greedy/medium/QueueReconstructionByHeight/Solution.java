package leetcode.greedy.medium.QueueReconstructionByHeight;


/*
Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example:
Given:
[7,1,5,3,6,4]
Result:
7
Explanation:
Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
*/
public class Solution {

    public int maxProfit(int[] prices) {
        int fullPrise = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i - 1] < prices[i]) {
                fullPrise += (prices[i] - prices[i - 1]);
            }
        }
        return fullPrise;
    }
}
