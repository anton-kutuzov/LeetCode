package leetcode.arrays.medium.BattleshipsInBoard;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        char[][] array = {
                {'X', '.', 'X', '.', 'X'},
                {'X', '.', '.', '.', 'X'},
                {'X', '.', 'X', 'X', '.'},
                {'.', '.', '.', '.', '.'},
                {'X', '.', 'X', '.', 'X'}
        };
        char[][] array2 = {{'X'}};
        char[][] array3 = {{'X'}, {'X'}};
        char[][] array4 = {{'X'}, {'.'}, {'X'}};
        char[][] array5 = {{'X', '.', 'X'}};
        char[][] array6 = {{'X', 'X'}};
        System.out.println(solution.countBattleships((array)) + " == 7");
        System.out.println(solution.countBattleships((array2)) + " == 1");
        System.out.println(solution.countBattleships((array3)) + " == 1");
        System.out.println(solution.countBattleships((array4)) + " == 2");
        System.out.println(solution.countBattleships((array5)) + " == 2");
        System.out.println(solution.countBattleships((array6)) + " == 1");
    }
}
