# LeetCode 2141. Maximum Running Time of N Computers — Hard
# https://leetcode.com/problems/maximum-running-time-of-n-computers/
# Submission 2201586006 — Accepted, Python3
#
# My thinking: in any window of T minutes a
# battery can give at most T minutes, so the
# whole room runs for T exactly when the
# capped-up total charge covers n times T —
# and that test only gets harder as T grows,
# so I binary-search the biggest T that passes.

class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        def feasible(t):
            return sum(min(b, t) for b in batteries) >= n * t

        lo, hi = 0, sum(batteries) // n + 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid
        return lo
