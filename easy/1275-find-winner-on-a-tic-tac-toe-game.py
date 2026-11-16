# LeetCode 1275. Find Winner on a Tic Tac Toe Game — Easy
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
# Submission 2197566556 — Accepted, Python3
#
# My thinking: I fill the 3x3 board from the moves —
# A plays X on even turns, B plays O on odd ones.
# Then I check all 8 winning lines (3 rows, 3
# columns, 2 diagonals). If nobody won and the
# board is full it is a draw, otherwise the game
# is still pending.

class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        grid = [[""] * 3 for _ in range(3)]
        for i, (r, c) in enumerate(moves):
            grid[r][c] = "X" if i % 2 == 0 else "O"
        lines = []
        for i in range(3):
            lines.append(grid[i])
            lines.append([grid[j][i] for j in range(3)])
        lines.append([grid[i][i] for i in range(3)])
        lines.append([grid[i][2 - i] for i in range(3)])
        for line in lines:
            if line == ["X", "X", "X"]:
                return "A"
            if line == ["O", "O", "O"]:
                return "B"
        return "Draw" if len(moves) == 9 else "Pending"
