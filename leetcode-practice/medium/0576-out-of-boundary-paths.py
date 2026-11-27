# LeetCode 576. Out of Boundary Paths — Medium
# https://leetcode.com/problems/out-of-boundary-paths/
# Submission 2198873860 — Accepted, Python3
#
# My thinking: I count how many ways the ball can
# be on each cell after each move. A step that
# leaves the grid adds to the answer; a step that
# stays inside carries its count forward.

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        total = 0
        for _ in range(maxMove):
            next_dp = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    if dp[r][c] == 0:
                        continue
                    for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                        if 0 <= nr < m and 0 <= nc < n:
                            next_dp[nr][nc] = (next_dp[nr][nc] + dp[r][c]) % MOD
                        else:
                            total = (total + dp[r][c]) % MOD
            dp = next_dp
        return total
