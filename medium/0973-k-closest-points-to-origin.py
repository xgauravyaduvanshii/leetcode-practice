# LeetCode 973. K Closest Points to Origin — Medium
# https://leetcode.com/problems/k-closest-points-to-origin/
# Submission 2198979644 — Accepted, Python3
#
# My thinking: I keep a heap of the k closest
# points I have seen, pushing each new point in
# and dropping the farthest whenever the heap
# grows too big. Distance is just x squared plus
# y squared — no square root needed.

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (-(x * x + y * y), [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [point for _, point in heap]
