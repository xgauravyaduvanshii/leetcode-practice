# LeetCode 768. Max Chunks To Make Sorted II — Hard
# https://leetcode.com/problems/max-chunks-to-make-sorted-ii/
# Submission 2198674864 — Accepted, Python3
#
# My thinking: a cut after position i works exactly
# when everything to the left is no bigger than
# everything to the right. I sweep once keeping the
# biggest value seen so far and comparing it against
# the smallest value still to come — every position
# where they line up is a chunk boundary.

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        suffix_min = [0] * (n + 1)
        suffix_min[n] = float("inf")
        for i in range(n - 1, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], arr[i])
        chunks = 0
        prefix_max = float("-inf")
        for i in range(n):
            prefix_max = max(prefix_max, arr[i])
            if prefix_max <= suffix_min[i + 1]:
                chunks += 1
        return chunks
