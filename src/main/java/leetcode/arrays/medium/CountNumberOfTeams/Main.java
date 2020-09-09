package leetcode.arrays.medium.CountNumberOfTeams;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        //int[] array = {1,2,3,4};
        //int[] array = {2,1,3}; //0
        //int[] array = {2,5,3,4,1}; //3
        int[] array = {1, 3, 2, 4, 5}; //7
        System.out.println(solution.numTeams(array));
    }
}
