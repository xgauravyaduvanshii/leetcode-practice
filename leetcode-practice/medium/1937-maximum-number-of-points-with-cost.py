# LeetCode 1937. Maximum Number of Points with Cost — Medium
# https://leetcode.com/problems/maximum-number-of-points-with-cost/
# Submission 2201707200 — Accepted, Python3
#
# My thinking: moving sideways costs a
# step per column, so from each row I sweep
# left and right carrying the best score
# so far, then add this row's points.

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points[0])
        dp = points[0][:]
        for row in points[1:]:
            left = [0] * n
            best = dp[0]
            for c in range(n):
                best = max(best, dp[c] + c)
                left[c] = best - c
            right = [0] * n
            best = dp[n - 1] - (n - 1)
            for c in range(n - 1, -1, -1):
                best = max(best, dp[c] - c)
                right[c] = best + c
            dp = [row[c] + max(left[c], right[c]) for c in range(n)]
        return max(dp)
