# LeetCode 1626. Best Team With No Conflicts — Medium
# https://leetcode.com/problems/best-team-with-no-conflicts/
# Submission 2199894925 — Accepted, Python3
#
# My thinking: after sorting by age, a valid
# team is a subsequence with non-decreasing
# scores. I build the best team ending at each
# player from the best teams ending earlier.

from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))
        n = len(players)
        dp = [0] * n
        best = 0
        for i in range(n):
            dp[i] = players[i][1]
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
            best = max(best, dp[i])
        return best
