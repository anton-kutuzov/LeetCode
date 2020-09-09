package leetcode.arrays.easy.PascalsTriangle;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/*
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Example:
Given:
5
Result:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Solution:
1. Added first line
2. Calculate next line by previous:
*/
public class Solution {

    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> listList = new ArrayList<>();
        if (numRows >= 1) {
            listList.add(Arrays.asList(1));
        }
        for (int i = 1; i < numRows; i++) {
            listList.add(generateLine(i, listList.get(i - 1)));
        }
        return listList;
    }

    private List<Integer> generateLine(int numOfLine, List<Integer> prev) {
        List<Integer> a = new ArrayList<>();
        a.add(1);
        for (int i = 1; i < numOfLine; i++) {
            a.add(prev.get(i - 1) + prev.get(i));
        }
        a.add(1);
        return a;
    }
}
