# LeetCode 174. Dungeon Game — Hard
# https://leetcode.com/problems/dungeon-game/
# Submission 2198391653 — Accepted, Python3
#
# My thinking: I work backwards from the princess.
# For each cell I ask how much health I need when I
# step into it: the smaller of the needs from the
# right and from below, minus what this cell gives
# or takes — and never less than one, because the
# knight must stay alive. The need at the start
# cell is the answer.

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        need = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            need[i][n] = float("inf")
        for j in range(n + 1):
            need[m][j] = float("inf")
        need[m][n - 1] = need[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                need[i][j] = max(1, min(need[i + 1][j], need[i][j + 1]) - dungeon[i][j])
        return need[0][0]
