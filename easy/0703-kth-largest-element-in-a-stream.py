# LeetCode 703. Kth Largest Element in a Stream — Easy
# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Submission 2197517483 — Accepted, Python3
#
# My thinking: I keep a min-heap of exactly k
# numbers — the k biggest ones I have seen. The
# smallest of those is the kth largest overall.
# When a new number arrives I push it in, and if
# the heap grows past k I drop the smallest.

import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
