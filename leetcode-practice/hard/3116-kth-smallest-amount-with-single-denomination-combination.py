# LeetCode 3116. Kth Smallest Amount With Single Denomination Combination — Hard
# https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/
# Submission 2202003982 — Accepted, Python3
#
# My thinking: I drop any coin that is
# a multiple of a smaller one, then
# build all subset LCMs with
# inclusion-exclusion signs. Those tell
# me how many numbers up to x are
# divisible by at least one coin, and
# that count only grows with x, so I
# binary-search the smallest x whose
# count reaches k.

from typing import List


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from math import gcd
        coins = sorted(set(coins))
        filt = []
        for c in coins:
            if any(c % d == 0 for d in filt):
                continue
            filt.append(c)
        coins = filt
        hi = k * coins[0]
        pairs = []
        for c in coins:
            new = [(c, 1)]
            for l, s in pairs:
                g = gcd(l, c)
                nl = l // g * c
                if nl <= hi:
                    new.append((nl, -s))
            pairs.extend(new)

        def count(x):
            total = 0
            for l, s in pairs:
                total += s * (x // l)
            return total

        lo = 1
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
