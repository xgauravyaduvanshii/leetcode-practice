# LeetCode 378. Kth Smallest Element in a Sorted Matrix — Medium
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# Submission 2198765113 — Accepted, Python3
#
# My thinking: every row is sorted, so the smallest
# unseen element is always the head of some row. I
# keep those heads in a heap, pop the smallest k - 1
# times — each time pushing the next element of that
# row — and the heap's top is the answer.

import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [(matrix[r][0], r, 0) for r in range(n)]
        heapq.heapify(heap)
        for _ in range(k - 1):
            _, r, c = heapq.heappop(heap)
            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
        return heap[0][0]
