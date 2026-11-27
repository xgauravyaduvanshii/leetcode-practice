# LeetCode 218. The Skyline Problem — Hard
# https://leetcode.com/problems/the-skyline-problem/
# Submission 2198395370 — Accepted, Python3
#
# My thinking: I sweep the buildings from left to
# right, turning each one into a start event that
# adds its height and an end event that removes it.
# A max-heap (with lazy removal of heights whose
# building has ended) always tells me the current
# skyline height. Whenever that height changes at
# an event's x, I write down the new skyline point.

import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))
        events.sort()
        skyline = []
        heap = [(0, float("inf"))]
        for x, neg_h, right in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)
            if neg_h:
                heapq.heappush(heap, (neg_h, right))
            top = -heap[0][0]
            if not skyline or skyline[-1][1] != top:
                skyline.append([x, top])
        return skyline
