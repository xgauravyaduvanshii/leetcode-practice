# LeetCode 1052. Grumpy Bookstore Owner — Medium
# https://leetcode.com/problems/grumpy-bookstore-owner/
# Submission 2198993578 — Accepted, Python3
#
# My thinking: the customers served while the
# owner is calm are already won. The secret
# technique covers one window of minutes, so I
# slide that window and keep the most grumpy
# minutes it can win back.

from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base = sum(c for c, g in zip(customers, grumpy) if g == 0)
        extra = 0
        window = 0
        for i, (c, g) in enumerate(zip(customers, grumpy)):
            if g == 1:
                window += c
            if i >= minutes and grumpy[i - minutes] == 1:
                window -= customers[i - minutes]
            extra = max(extra, window)
        return base + extra
