# LeetCode 837. New 21 Game — Medium
# https://leetcode.com/problems/new-21-game/
# Submission 2198951667 — Accepted, Python3
#
# My thinking: the chance of landing on each
# score is the average of the chances of the
# previous maxPts scores. A sliding window keeps
# that average, and adding up the chances from k
# to n gives the answer.

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window = 1.0
        for i in range(1, n + 1):
            dp[i] = window / maxPts
            if i < k:
                window += dp[i]
            if i - maxPts >= 0:
                window -= dp[i - maxPts]
        return sum(dp[k:])
