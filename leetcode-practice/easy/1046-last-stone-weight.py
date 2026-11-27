# LeetCode 1046. Last Stone Weight — Easy
# https://leetcode.com/problems/last-stone-weight/
# Submission 2197554007 — Accepted, Python3
#
# My thinking: I always smash the two heaviest
# stones together. A max-heap (stored as negatives
# in Python's min-heap) gives me the heaviest two
# each time. If they are equal, both vanish; if
# not, the difference goes back in as a new stone.
# When one stone is left, that is the answer.

import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -(y - x))
        return -heap[0] if heap else 0
