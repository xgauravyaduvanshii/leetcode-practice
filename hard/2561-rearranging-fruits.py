# LeetCode 2561. Rearranging Fruits — Hard
# https://leetcode.com/problems/rearranging-fruits/
# Submission 2201821442 — Accepted, Python3
#
# My thinking: a fruit can only be
# balanced if it appears an even number
# of times overall, so I gather what
# each basket has too much of, pair the
# cheapest spares together, and pay the
# smaller of a straight swap or two
# trips through the cheapest fruit of
# all.

from collections import Counter


class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        c1 = Counter(basket1)
        c2 = Counter(basket2)
        total = c1 + c2
        for v in total.values():
            if v % 2:
                return -1
        swap1, swap2 = [], []
        for v, t in total.items():
            half = t // 2
            if c1[v] > half:
                swap1.extend([v] * (c1[v] - half))
            if c2[v] > half:
                swap2.extend([v] * (c2[v] - half))
        swap1.sort()
        swap2.sort()
        cheapest = min(total)
        ans = 0
        for a, b in zip(swap1, swap2):
            ans += min(min(a, b), 2 * cheapest)
        return ans
