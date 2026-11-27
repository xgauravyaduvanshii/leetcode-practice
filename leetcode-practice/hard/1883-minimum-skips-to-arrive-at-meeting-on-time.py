# LeetCode 1883. Minimum Skips to Arrive at Meeting On Time — Hard
# https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/
# Submission 2201215127 — Accepted, Python3
#
# My thinking: I walk the roads keeping, for
# every number of skips used, the earliest I can
# arrive — skipping a rest just carries the raw
# driving time forward, resting rounds it up to
# the next whole hour.

import math

class Solution:
    def minSkips(self, dist: list[int], speed: int, hoursBefore: float) -> int:
        n = len(dist)
        INF = float("inf")
        dp = [INF] * (n + 1)
        dp[0] = 0.0
        for i, d in enumerate(dist):
            ndp = [INF] * (n + 1)
            for j in range(n + 1):
                if dp[j] == INF:
                    continue
                t = dp[j] + d / speed
                if i < n - 1:
                    ndp[j] = min(ndp[j], math.ceil(t - 1e-9))
                else:
                    ndp[j] = min(ndp[j], t)
                if j + 1 <= n:
                    ndp[j + 1] = min(ndp[j + 1], t)
            dp = ndp
        for j in range(n + 1):
            if dp[j] <= hoursBefore + 1e-9:
                return j
        return -1
