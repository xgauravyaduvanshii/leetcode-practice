# LeetCode 1029. Two City Scheduling — Medium
# https://leetcode.com/problems/two-city-scheduling/
# Submission 2198989490 — Accepted, Python3
#
# My thinking: I sort people by how much cheaper
# city A is than city B. The first half go to A
# and the rest to B — that is the cheapest split.

from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda pair: pair[0] - pair[1])
        n = len(costs) // 2
        total = 0
        for i, (a, b) in enumerate(costs):
            total += a if i < n else b
        return total
