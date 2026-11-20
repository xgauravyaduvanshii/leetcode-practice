# LeetCode 1824. Minimum Sideway Jumps — Medium
# https://leetcode.com/problems/minimum-sideway-jumps/
# Submission 2199941967 — Accepted, Python3
#
# My thinking: I walk the track keeping the
# cheapest jump count for each lane. A lane
# with an obstacle becomes unreachable, and
# any open lane can always switch from the
# cheapest lane for one extra jump.

from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        INF = float("inf")
        jumps = [1, 0, 1]
        for obstacle in obstacles[1:]:
            for lane in range(3):
                if obstacle == lane + 1:
                    jumps[lane] = INF
            best = min(jumps)
            for lane in range(3):
                if obstacle != lane + 1:
                    jumps[lane] = min(jumps[lane], best + 1)
        return min(jumps)
