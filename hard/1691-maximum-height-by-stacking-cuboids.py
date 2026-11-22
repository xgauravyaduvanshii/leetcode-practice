# LeetCode 1691. Maximum Height by Stacking Cuboids — Hard
# https://leetcode.com/problems/maximum-height-by-stacking-cuboids/
# Submission 2201094349 — Accepted, Python3
#
# My thinking: I sort every cuboid's sides so each one
# can only sit one way, sort the cuboids themselves, and
# then run a longest-chain search where a cuboid may sit
# on another only when all three of its sides fit.

class Solution:
    def maxHeight(self, cuboids: list[list[int]]) -> int:
        cuboids = [sorted(c) for c in cuboids]
        cuboids.sort()
        n = len(cuboids)
        dp = [0] * n
        best = 0
        for i in range(n):
            dp[i] = cuboids[i][2]
            for j in range(i):
                if (cuboids[j][0] <= cuboids[i][0]
                        and cuboids[j][1] <= cuboids[i][1]
                        and cuboids[j][2] <= cuboids[i][2]):
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])
            best = max(best, dp[i])
        return best
