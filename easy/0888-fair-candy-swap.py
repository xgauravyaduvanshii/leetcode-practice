# LeetCode 888. Fair Candy Swap — Easy
# https://leetcode.com/problems/fair-candy-swap/
# Submission 2197538484 — Accepted, Python3
#
# My thinking: after the swap both totals have to be
# equal, so Alice needs to give away half of the
# difference between their totals. For each of her
# boxes, the box Bob must give back is that much
# smaller — if Bob has a box of that size, the
# swap works.

class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)
        diff = (sum_a - sum_b) // 2
        bob_set = set(bobSizes)
        for x in aliceSizes:
            y = x - diff
            if y in bob_set:
                return [x, y]
        return []
