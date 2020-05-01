package leetcode.arrays.medium.RotateImage;


/*
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example:
Given:
matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
Result:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
 */
public class Solution {

    public void rotate(int[][] matrix) {
        int tmp;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = i + 1; j < matrix.length; j++) {
                tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        }
        for (int[] ints : matrix) {
            reverse(ints, 0, ints.length - 1);
        }
    }

    private void reverse(int[] row, int i, int j) {
        int tmp;
        while (i < j) {
            tmp = row[i];
            row[i] = row[j];
            row[j] = tmp;
            i++;
            j--;
        }
    }
}
