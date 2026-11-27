# LeetCode 1642. Furthest Building You Can Reach — Medium
# https://leetcode.com/problems/furthest-building-you-can-reach/
# Submission 2199900270 — Accepted, Python3
#
# My thinking: ladders belong on the biggest
# climbs. I keep every climb in a min-heap and
# pay bricks for the smallest ones; when the
# bricks run out, I am stuck.

import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        climbs = []
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue
            heapq.heappush(climbs, climb)
            if len(climbs) > ladders:
                bricks -= heapq.heappop(climbs)
            if bricks < 0:
                return i
        return len(heights) - 1
