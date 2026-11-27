# LeetCode 769. Max Chunks To Make Sorted — Medium
# https://leetcode.com/problems/max-chunks-to-make-sorted/
# Submission 2198931813 — Accepted, Python3
#
# My thinking: the array is a permutation of
# 0..n-1, so a chunk can end exactly where the
# biggest value seen so far equals the index —
# everything to the left already belongs there.

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        biggest = 0
        for i, num in enumerate(arr):
            biggest = max(biggest, num)
            if biggest == i:
                chunks += 1
        return chunks
