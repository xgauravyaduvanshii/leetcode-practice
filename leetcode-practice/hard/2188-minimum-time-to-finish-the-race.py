# LeetCode 2188. Minimum Time to Finish the Race — Hard
# https://leetcode.com/problems/minimum-time-to-finish-the-race/
# Submission 2201605391 — Accepted, Python3
#
# My thinking: a set of tyres only gets
# slower, so no stint is ever worth more
# than a handful of laps — I price the best
# stint of each length once, then chain
# stints together, paying the change each
# time except the first.

class Solution:
    def minimumFinishTime(self, tires: list[list[int]], changeTime: int, numLaps: int) -> int:
        min_f = min(f for f, _ in tires)
        # Best time for a stint of x laps on one set of tyres.
        best = [float('inf')] * 19
        for f, r in tires:
            t = 0
            cur = f
            for x in range(1, 19):
                t += cur
                best[x] = min(best[x], t)
                if cur > changeTime + min_f:
                    break
                cur *= r
        INF = float('inf')
        dp = [INF] * (numLaps + 1)
        dp[0] = -changeTime
        for i in range(1, numLaps + 1):
            for x in range(1, min(i, 18) + 1):
                if best[x] < INF:
                    dp[i] = min(dp[i], dp[i - x] + best[x] + changeTime)
        return dp[numLaps]
