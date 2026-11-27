# LeetCode 215. Kth Largest Element in an Array — Medium
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Submission 2198455822 — Accepted, Python3
#
# My thinking: I keep a small heap of the k biggest
# numbers seen so far. Each new number goes in,
# and if the heap grows past k the smallest of them
# drops out. At the end the smallest number in the
# heap is exactly the kth largest overall.

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
