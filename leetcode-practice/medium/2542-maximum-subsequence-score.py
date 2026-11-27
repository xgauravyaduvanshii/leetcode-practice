# LeetCode 2542. Maximum Subsequence Score — Medium
# https://leetcode.com/problems/maximum-subsequence-score/
# Submission 2200986348 — Accepted, Python3
#
# My thinking: I sort the pairs by the second number and
# sweep down from the biggest — every pair I pass can be
# the minimum, so I keep the k biggest first numbers so
# far and take the best product.

import heapq


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)
        heap = []
        total = 0
        best = 0
        for second, first in pairs:
            heapq.heappush(heap, first)
            total += first
            if len(heap) > k:
                total -= heapq.heappop(heap)
            if len(heap) == k:
                best = max(best, total * second)
        return best
