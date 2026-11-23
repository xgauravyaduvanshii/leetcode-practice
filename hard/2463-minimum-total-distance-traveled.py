# LeetCode 2463. Minimum Total Distance Traveled — Hard
# https://leetcode.com/problems/minimum-total-distance-traveled/
# Submission 2201762222 — Accepted, Python3
#
# My thinking: robots and factories both
# line up in order, so a factory only ever
# takes the next few robots in line — I
# sort both, then fill a table where each
# factory either sits out or takes a run
# of the robots still waiting, using a
# running prefix so the cost of each run
# is one subtraction.

class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort()
        n = len(robot)
        m = len(factory)
        INF = float("inf")
        dp = [[INF] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for j in range(1, m + 1):
            pos, limit = factory[j - 1]
            dp[0][j] = 0
            for i in range(1, n + 1):
                best = dp[i][j - 1]
                # factory j takes the last t robots (1..limit)
                run = 0
                for t in range(1, min(limit, i) + 1):
                    run += abs(robot[i - t] - pos)
                    if dp[i - t][j - 1] != INF:
                        best = min(best, dp[i - t][j - 1] + run)
                dp[i][j] = best
        return dp[n][m]
