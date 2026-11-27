# LeetCode 835. Image Overlap — Medium
# https://leetcode.com/problems/image-overlap/
# Submission 2198950999 — Accepted, Python3
#
# My thinking: sliding one image over the other
# only changes which ones line up. For every pair
# of ones I record the shift between them — the
# shift that appears most often is the best
# overlap.

from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        shifts = {}
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift = (r2 - r1, c2 - c1)
                shifts[shift] = shifts.get(shift, 0) + 1
        return max(shifts.values(), default=0)
