# LeetCode 1093. Statistics from a Large Sample — Medium
# https://leetcode.com/problems/statistics-from-a-large-sample/
# Submission 2198997674 — Accepted, Python3
#
# My thinking: the minimum and maximum are the
# first and last non-zero counts, the mean is
# the weighted average, and the mode is the
# biggest count. For the median I walk the
# counts until I pass the middle one — or the
# middle two, and average them.

from typing import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        total = sum(count)
        minimum = next(i for i, c in enumerate(count) if c > 0)
        maximum = next(i for i in range(255, -1, -1) if count[i] > 0)
        mean = sum(i * c for i, c in enumerate(count)) / total
        mode = count.index(max(count))
        first = (total + 1) // 2
        second = total // 2 + 1
        seen = 0
        low = high = None
        for i, c in enumerate(count):
            seen += c
            if low is None and seen >= first:
                low = i
            if seen >= second:
                high = i
                break
        median = (low + high) / 2
        return [float(minimum), float(maximum), mean, median, float(mode)]
