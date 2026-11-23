# LeetCode 3219. Minimum Cost for Cutting Cake II — Hard
# https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/
# Submission 2202098852 — Accepted, Python3
#
# My thinking: cutting the more expensive
# line first is always better, because
# its cost is multiplied by fewer pieces.
# I sort both cut lists descending and
# take the larger next cut each time,
# multiplying by how many pieces the
# other direction already has.

from typing import List


class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        h_pieces = 1
        v_pieces = 1
        i = 0
        j = 0
        total = 0
        while i < len(horizontalCut) or j < len(verticalCut):
            if j == len(verticalCut) or (i < len(horizontalCut) and horizontalCut[i] > verticalCut[j]):
                total += horizontalCut[i] * v_pieces
                h_pieces += 1
                i += 1
            else:
                total += verticalCut[j] * h_pieces
                v_pieces += 1
                j += 1
        return total
