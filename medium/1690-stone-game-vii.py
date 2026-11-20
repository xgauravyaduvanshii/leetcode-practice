# LeetCode 1690. Stone Game VII — Medium
# https://leetcode.com/problems/stone-game-vii/
# Submission 2199913512 — Accepted, Python3
#
# My thinking: whoever moves takes the end
# stones and scores the rest. I work out the
# best difference over every interval, from
# the shortest to the longest.

from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0]
        for stone in stones:
            prefix.append(prefix[-1] + stone)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(prefix[j + 1] - prefix[i + 1] - dp[i + 1][j],
                               prefix[j] - prefix[i] - dp[i][j - 1])
        return dp[0][n - 1]
