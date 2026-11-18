# LeetCode 373. Find K Pairs with Smallest Sums — Medium
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
# Submission 2198759914 — Accepted, Python3
#
# My thinking: the smallest pair starts at the
# fronts of both arrays. I keep a heap of the best
# pair for each first element, pop the smallest one,
# and push the next partner from the second array —
# that walks the pairs out in order.

import heapq
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        heap = []
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        pairs = []
        while heap and len(pairs) < k:
            _, i, j = heapq.heappop(heap)
            pairs.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return pairs
