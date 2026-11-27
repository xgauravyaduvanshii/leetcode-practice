# LeetCode 986. Interval List Intersections — Medium
# https://leetcode.com/problems/interval-list-intersections/
# Submission 2198982342 — Accepted, Python3
#
# My thinking: I walk both lists together. The
# overlap of the two current intervals is where
# they both cover, and I move past whichever one
# ends first.

from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start <= end:
                result.append([start, end])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return result
