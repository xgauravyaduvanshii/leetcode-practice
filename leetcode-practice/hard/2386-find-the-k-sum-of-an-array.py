# LeetCode 2386. Find the K-Sum of an Array — Hard
# https://leetcode.com/problems/find-the-k-sum-of-an-array/
# Submission 2201711103 — Accepted, Python3
#
# My thinking: the biggest sum takes every
# positive number, and every smaller sum
# is that total minus some loss — I grow
# the smallest losses with a heap and
# subtract the (k - 1)-th one.

import heapq


class Solution:
    def kSum(self, nums: list[int], k: int) -> int:
        total = sum(x for x in nums if x > 0)
        if k == 1:
            return total
        vals = sorted(abs(x) for x in nums)
        heap = [(vals[0], 0)]
        loss = 0
        for _ in range(k - 1):
            loss, i = heapq.heappop(heap)
            if i + 1 < len(vals):
                heapq.heappush(heap, (loss + vals[i + 1], i + 1))
                heapq.heappush(heap, (loss - vals[i] + vals[i + 1], i + 1))
        return total - loss
