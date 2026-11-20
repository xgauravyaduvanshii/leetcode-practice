# LeetCode 1562. Find Latest Group of Size M — Medium
# https://leetcode.com/problems/find-latest-group-of-size-m/
# Submission 2199877463 — Accepted, Python3
#
# My thinking: each new 1 merges its neighbors
# into one group. I track every group's length
# at its two ends, so merging is constant
# time, and I remember the last step where a
# group of size m existed.

from typing import List


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return n
        lengths = [0] * (n + 2)
        counts = {}
        latest = -1
        for step, pos in enumerate(arr, 1):
            left = lengths[pos - 1]
            right = lengths[pos + 1]
            length = left + right + 1
            lengths[pos - left] = length
            lengths[pos + right] = length
            if left:
                counts[left] -= 1
            if right:
                counts[right] -= 1
            counts[length] = counts.get(length, 0) + 1
            if counts.get(m, 0) > 0:
                latest = step
        return latest
