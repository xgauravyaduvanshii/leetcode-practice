# LeetCode 2790. Maximum Number of Groups With Increasing Length — Hard
# https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/
# Submission 2201615972 — Accepted, Python3
#
# My thinking: k groups must have strictly
# increasing sizes, so the smallest they can
# be is 1, 2, ..., k — and a number used at
# most L times can give at most one slot to
# each group, so for every t the t biggest
# groups need sum min(limit, t) to cover
# their sizes. That check is monotone in k,
# so I binary-search the biggest k that
# passes it for every t.

class Solution:
    def maximumGroups(self, usageLimits: list[int]) -> int:
        limits = sorted(usageLimits)
        n = len(limits)
        pref = [0]
        for x in limits:
            pref.append(pref[-1] + x)

        def feasible(k: int) -> bool:
            # j counts the limits <= t; it only moves forward
            # as t grows, so this whole check is O(n + k).
            j = 0
            for t in range(1, k + 1):
                while j < n and limits[j] <= t:
                    j += 1
                have = pref[j] + t * (n - j)
                need = t * (2 * k - t + 1) // 2
                if have < need:
                    return False
            return True

        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
