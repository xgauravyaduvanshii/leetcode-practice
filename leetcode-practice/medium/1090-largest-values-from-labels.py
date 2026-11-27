# LeetCode 1090. Largest Values From Labels — Medium
# https://leetcode.com/problems/largest-values-from-labels/
# Submission 2198997353 — Accepted, Python3
#
# My thinking: I take the items in order of
# value, biggest first, and keep each one unless
# its label has already been used as often as
# allowed.

from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        items = sorted(zip(values, labels), reverse=True)
        used = {}
        total = 0
        picked = 0
        for value, label in items:
            if picked == numWanted:
                break
            if used.get(label, 0) >= useLimit:
                continue
            used[label] = used.get(label, 0) + 1
            total += value
            picked += 1
        return total
