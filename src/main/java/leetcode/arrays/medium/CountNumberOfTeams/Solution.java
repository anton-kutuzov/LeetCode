package leetcode.arrays.medium.CountNumberOfTeams;


/*
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
You have to form a team of 3 soldiers amongst them under the following rules:
    Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
    A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Example:
Given:
rating = [2,5,3,4,1]
Result:
3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).
*/
public class Solution {

    public int numTeams(int[] rating) {
        int count = 0;
        for (int i = 1; i < rating.length - 1; i++) {
            int leftLess = 0;
            int rightLess = 0;
            int leftGather = 0;
            int rightGather = 0;
            for (int j = 0; j < i; j++) {
                if (rating[i] > rating[j]) {
                    leftGather++;
                } else if (rating[i] < rating[j]) {
                    leftLess++;
                }
            }
            for (int j = i + 1; j < rating.length; j++) {
                if (rating[i] > rating[j]) {
                    rightGather++;
                } else if (rating[i] < rating[j]) {
                    rightLess++;
                }
            }
            count += rightGather * leftLess + rightLess * leftGather;
        }
        return count;
    }

    public int numTeams2(int[] rating) {
        int count = 0;
        for (int i = 0; i < rating.length - 2; i++) {
            for (int j = i + 1; j < rating.length - 1; j++) {
                for (int k = j + 1; k < rating.length; k++) {
                    if ((rating[i] > rating[j] && rating[j] > rating[k]) ||
                            (rating[i] < rating[j] && rating[j] < rating[k])) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}
