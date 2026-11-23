# LeetCode 2218. Maximum Value of K Coins From Piles — Hard
# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
# Submission 2201626066 — Accepted, Python3
#
# My thinking: coins come off the top of
# each pile in order, so I price every pile
# by how many I take from it, then share
# exactly k coins across the piles for the
# best total.

class Solution:
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:
        prefs = []
        for pile in piles:
            pref = [0]
            for c in pile:
                pref.append(pref[-1] + c)
            prefs.append(pref)
        dp = [0] * (k + 1)
        for pref in prefs:
            new_dp = [0] * (k + 1)
            for j in range(k + 1):
                best = dp[j]
                for t in range(1, min(len(pref) - 1, j) + 1):
                    best = max(best, dp[j - t] + pref[t])
                new_dp[j] = best
            dp = new_dp
        return dp[k]
