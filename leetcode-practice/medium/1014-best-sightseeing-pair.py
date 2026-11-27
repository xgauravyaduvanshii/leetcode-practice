# LeetCode 1014. Best Sightseeing Pair — Medium
# https://leetcode.com/problems/best-sightseeing-pair/
# Submission 2198986489 — Accepted, Python3
#
# My thinking: for each spot I only need the best
# earlier spot, scored as its value plus its
# position. The pair score is that best earlier
# value plus this spot's value minus its
# position.

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best = 0
        best_left = values[0]
        for j in range(1, len(values)):
            best = max(best, best_left + values[j] - j)
            best_left = max(best_left, values[j] + j)
        return best
