# LeetCode 2528. Maximize the Minimum Powered City — Hard
# https://leetcode.com/problems/maximize-the-minimum-powered-city/
# Submission 2201797567 — Accepted, Python3
#
# My thinking: the answer only grows
# one way, so I binary-search it — for
# a target I walk the cities left to
# right, and whenever one falls short I
# plant the missing stations as far
# right as they still reach it, so they
# help the most cities ahead.

class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        n = len(stations)
        prefix = [0] * (n + 1)
        for i, x in enumerate(stations):
            prefix[i + 1] = prefix[i] + x

        def power(i):
            lo = max(0, i - r)
            hi = min(n - 1, i + r)
            return prefix[hi + 1] - prefix[lo]

        def feasible(target):
            added = [0] * (n + 1)
            used = 0
            running = 0
            for i in range(n):
                running += added[i]
                cur = power(i) + running
                if cur < target:
                    need = target - cur
                    used += need
                    if used > k:
                        return False
                    pos = min(n - 1, i + r)
                    # the new stations reach back to i, so count them now
                    running += need
                    # they stop helping after pos + r
                    if pos + r + 1 < n:
                        added[pos + r + 1] -= need
            return used <= k

        lo, hi = 0, sum(stations) + k + 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
