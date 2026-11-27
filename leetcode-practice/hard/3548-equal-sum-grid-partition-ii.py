# LeetCode 3548. Equal Sum Grid Partition II — Hard
# https://leetcode.com/problems/equal-sum-grid-partition-ii/
# Submission 2202835971 — Accepted, Python3
from typing import List
from collections import Counter


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # My thinking: a cut splits the grid into two rectangles. If
        # their sums already match, that cut works. Otherwise the
        # larger side must lose exactly the difference by dropping
        # one cell, and the rest of that side must stay connected.
        # A rectangle with both sides at least 2 stays connected
        # after any single cell is removed, so there I only need a
        # cell with the right value — I keep running frequency maps
        # while sweeping the cuts. A one-row or one-column side only
        # survives losing an end cell, so there I check just the two
        # ends. A single cell can never be dropped.
        m = len(grid)
        n = len(grid[0])
        total = sum(sum(r) for r in grid)
        row_sum = [sum(r) for r in grid]
        pref = [0]
        for s in row_sum:
            pref.append(pref[-1] + s)
        top_freq: Counter = Counter()
        bot_freq: Counter = Counter()
        for r in grid:
            bot_freq.update(r)
        for i in range(m - 1):
            top_freq.update(grid[i])
            for v in grid[i]:
                bot_freq[v] -= 1
                if bot_freq[v] == 0:
                    del bot_freq[v]
            s_top = pref[i + 1]
            s_bot = total - s_top
            if s_top == s_bot:
                return True
            if s_top > s_bot:
                if self._removable(grid, 0, i, 0, n - 1, s_top - s_bot, top_freq):
                    return True
            else:
                if self._removable(grid, i + 1, m - 1, 0, n - 1, s_bot - s_top, bot_freq):
                    return True
        col_sum = [sum(grid[r][c] for r in range(m)) for c in range(n)]
        prefc = [0]
        for s in col_sum:
            prefc.append(prefc[-1] + s)
        left_freq: Counter = Counter()
        right_freq: Counter = Counter()
        for r in grid:
            right_freq.update(r)
        for j in range(n - 1):
            for r in range(m):
                v = grid[r][j]
                left_freq[v] += 1
                right_freq[v] -= 1
                if right_freq[v] == 0:
                    del right_freq[v]
            s_left = prefc[j + 1]
            s_right = total - s_left
            if s_left == s_right:
                return True
            if s_left > s_right:
                if self._removable(grid, 0, m - 1, 0, j, s_left - s_right, left_freq):
                    return True
            else:
                if self._removable(grid, 0, m - 1, j + 1, n - 1, s_right - s_left, right_freq):
                    return True
        return False

    @staticmethod
    def _removable(grid, r1, r2, c1, c2, diff, freq):
        h = r2 - r1 + 1
        w = c2 - c1 + 1
        if h == 1 and w == 1:
            return False
        if h == 1:
            return grid[r1][c1] == diff or grid[r1][c2] == diff
        if w == 1:
            return grid[r1][c1] == diff or grid[r2][c1] == diff
        return freq.get(diff, 0) > 0
