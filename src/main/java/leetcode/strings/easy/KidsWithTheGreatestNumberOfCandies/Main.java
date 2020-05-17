package leetcode.strings.easy.KidsWithTheGreatestNumberOfCandies;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] candies = {2,3,5,1,3};
        int extraCandies = 3;
        System.out.println(solution.kidsWithCandies(candies, extraCandies));
    }
}
