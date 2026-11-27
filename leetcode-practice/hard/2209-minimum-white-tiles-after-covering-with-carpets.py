# LeetCode 2209. Minimum White Tiles After Covering With Carpets — Hard
# https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/
# Submission 2201618578 — Accepted, Python3
#
# My thinking: I walk the floor tile by tile
# — each tile either stays visible or gets
# covered by a carpet ending here, and the
# cheapest choice at every tile with every
# carpet count is the answer.

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        INF = float('inf')
        dp = [[INF] * (numCarpets + 1) for _ in range(n + 1)]
        for k in range(numCarpets + 1):
            dp[0][k] = 0
        for i in range(1, n + 1):
            white = 1 if floor[i - 1] == '1' else 0
            for k in range(numCarpets + 1):
                dp[i][k] = dp[i - 1][k] + white
                if k > 0:
                    dp[i][k] = min(dp[i][k], dp[max(0, i - carpetLen)][k - 1])
        return dp[n][numCarpets]
