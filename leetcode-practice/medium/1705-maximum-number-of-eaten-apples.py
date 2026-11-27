# LeetCode 1705. Maximum Number of Eaten Apples — Medium
# https://leetcode.com/problems/maximum-number-of-eaten-apples/
# Submission 2199915460 — Accepted, Python3
#
# My thinking: every day I eat one apple from
# the batch that rots soonest. A min-heap
# ordered by expiry keeps that batch on top,
# and rotten batches drop out before I eat.

import heapq
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []
        eaten = 0
        day = 0
        n = len(apples)
        while day < n or heap:
            if day < n and apples[day] > 0:
                heapq.heappush(heap, (day + days[day], apples[day]))
            while heap and heap[0][0] <= day:
                heapq.heappop(heap)
            if heap:
                expiry, count = heapq.heappop(heap)
                eaten += 1
                if count > 1:
                    heapq.heappush(heap, (expiry, count - 1))
            day += 1
        return eaten
