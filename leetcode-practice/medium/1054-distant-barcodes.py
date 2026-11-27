# LeetCode 1054. Distant Barcodes — Medium
# https://leetcode.com/problems/distant-barcodes/
# Submission 2198993992 — Accepted, Python3
#
# My thinking: I lay out the most common barcode
# first, spacing its copies two apart, then fill
# the remaining slots with the rest in the same
# way. Spreading each value out guarantees no
# two neighbours ever match.

from collections import Counter
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counts = Counter(barcodes)
        ordered = sorted(counts, key=lambda code: -counts[code])
        result = [0] * len(barcodes)
        index = 0
        for code in ordered:
            for _ in range(counts[code]):
                result[index] = code
                index += 2
                if index >= len(barcodes):
                    index = 1
        return result
