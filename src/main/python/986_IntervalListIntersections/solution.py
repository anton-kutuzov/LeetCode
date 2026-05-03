"""LeetCode 986. Interval List Intersections

https://leetcode.com/problems/interval-list-intersections/
"""

from __future__ import annotations
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_index = 0
        second_index = 0

        answer = []

        num_of_first_intervals = len(firstList)
        num_of_second_intervals = len(secondList)
        while first_index < num_of_first_intervals and second_index < num_of_second_intervals:
            first_current_interval = firstList[first_index]
            second_current_interval = secondList[second_index]

            start = max(first_current_interval[0], second_current_interval[0])
            end = min(first_current_interval[1], second_current_interval[1])

            if start <= end:
                answer.append([start, end])

            if end >= first_current_interval[1]:
                first_index += 1

            if end >= second_current_interval[1]:
                second_index += 1

        return answer
