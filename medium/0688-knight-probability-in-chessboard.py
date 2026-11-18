# LeetCode 688. Knight Probability in Chessboard — Medium
# https://leetcode.com/problems/knight-probability-in-chessboard/
# Submission 2198910727 — Accepted, Python3
#
# My thinking: I track the chance of the knight
# being on each square after every move. Each move
# splits a square's chance eight ways, and only
# the shares that stay on the board survive.

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        for _ in range(k):
            next_dp = [[0.0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if dp[r][c] == 0:
                        continue
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            next_dp[nr][nc] += dp[r][c] / 8
            dp = next_dp
        return sum(sum(row_values) for row_values in dp)
