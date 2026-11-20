# 3095. Shortest Subarray With OR at Least K I (Easy)
# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/
# Submission 2199974792 — Accepted, Python3
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # My thinking: try every starting spot and grow
        # the subarray to the right, keeping the running
        # OR. The first end that reaches k gives the
        # shortest subarray from that start — and the
        # best of those over all starts is the answer.
        n = len(nums)
        best = float("inf")
        for start in range(n):
            value = 0
            for end in range(start, n):
                value |= nums[end]
                if value >= k:
                    best = min(best, end - start + 1)
                    break
        return -1 if best == float("inf") else best
