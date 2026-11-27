# LeetCode 1889. Minimum Space Wasted From Packaging — Hard
# https://leetcode.com/problems/minimum-space-wasted-from-packaging/
# Submission 2201217580 — Accepted, Python3
#
# My thinking: I pick one supplier, and every
# package takes the smallest box of theirs that
# fits it — so I sort the packages, walk each
# supplier's box sizes in order, and add up the
# waste band by band.

import bisect

MOD = 10 ** 9 + 7

class Solution:
    def minWastedSpace(self, packages: list[int], boxes: list[list[int]]) -> int:
        packages.sort()
        n = len(packages)
        pref = [0] * (n + 1)
        for i, p in enumerate(packages):
            pref[i + 1] = pref[i] + p
        ans = float("inf")
        for supplier in boxes:
            supplier.sort()
            if supplier[-1] < packages[-1]:
                continue
            waste = 0
            prev = 0
            for b in supplier:
                idx = bisect.bisect_right(packages, b, prev)
                waste += (idx - prev) * b - (pref[idx] - pref[prev])
                prev = idx
                if prev == n:
                    break
            if prev == n:
                ans = min(ans, waste)
        return -1 if ans == float("inf") else ans % MOD
