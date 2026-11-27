# LeetCode 2558. Take Gifts From the Richest Pile — Easy
# https://leetcode.com/problems/take-gifts-from-the-richest-pile/
# Submission 2197802219 — Accepted, Python3
#
# My thinking: each second I take from the biggest
# pile and leave the square root of what was there.
# A max-heap (stored as negatives) always gives me
# the biggest pile in O(log n).

import heapq
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-g for g in gifts]
        heapq.heapify(heap)
        for _ in range(k):
            m = -heapq.heappop(heap)
            heapq.heappush(heap, -math.isqrt(m))
        return -sum(heap)
