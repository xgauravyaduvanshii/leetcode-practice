# LeetCode 1792. Maximum Average Pass Ratio — Medium
# https://leetcode.com/problems/maximum-average-pass-ratio/
# Submission 2199935178 — Accepted, Python3
#
# My thinking: each extra student helps most
# in the class where the ratio jumps the most.
# A max-heap always hands the next student to
# that class.

import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t

        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)
        for _ in range(extraStudents):
            _, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))
        return sum(p / t for _, p, t in heap) / len(classes)
