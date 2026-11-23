# LeetCode 2167. Minimum Time to Remove All Cars Containing Illegal Goods — Hard
# https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/
# Submission 2201598422 — Accepted, Python3
#
# My thinking: the cars in the middle are
# cheapest pulled out where they stand at two
# a piece, while the ends come off one a
# piece — so I keep a middle stretch, pay the
# ends to reach it, and let the cheapest
# left-hand start win as the stretch grows.

class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        ones = [i for i, c in enumerate(s) if c == '1']
        if not ones:
            return 0
        prefix = [0] * (n + 1)
        for i, c in enumerate(s):
            prefix[i + 1] = prefix[i] + (c == '1')
        best = 2 * len(ones)
        min_left = 0
        for r in range(n):
            min_left = min(min_left, r - 2 * prefix[r])
            cost = min_left + (n - 1 - r) + 2 * prefix[r + 1]
            best = min(best, cost)
        best = min(best, ones[-1] + 1, n - ones[0])
        return best
