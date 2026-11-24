# LeetCode 3459. Length of Longest V-Shaped Diagonal Segment — Hard
# https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/
# Submission 2202555405 — Accepted 561/561, Python3
from array import array
from typing import List


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        # My thinking: the values after the starting 1 must run
        # 2, 0, 2, 0, ..., so from any cell the next value is
        # forced by the current one — no step parity needs
        # storing. I first tabulate, per diagonal direction,
        # the straight alternating run from each cell. Then,
        # per direction, a second table adds the best option of
        # going straight or turning once clockwise, both read
        # from tables already filled by walking each diagonal
        # backwards. Flat unsigned-short arrays keep the memory
        # small, which a cached recursion could not.
        n = len(grid)
        m = len(grid[0])
        # Clockwise diagonal order: SE, SW, NW, NE, so a turn
        # is (d + 1) % 4.
        dirs = ((1, 1), (1, -1), (-1, -1), (-1, 1))

        def order(di, dj):
            rows = range(n - 1, -1, -1) if di == 1 else range(n)
            cols = range(m - 1, -1, -1) if dj == 1 else range(m)
            return rows, cols

        # g[d][i * m + j]: straight alternating run starting
        # at (i, j) in direction d (0 unless grid is 0 or 2).
        g = []
        for d in range(4):
            di, dj = dirs[d]
            tab = array("H", bytes(2 * n * m))
            rows, cols = order(di, dj)
            for i in rows:
                for j in cols:
                    v = grid[i][j]
                    if v != 0 and v != 2:
                        continue
                    ni, nj = i + di, j + dj
                    nxt = 0 if v == 2 else 2
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == nxt:
                        tab[i * m + j] = 1 + tab[ni * m + nj]
                    else:
                        tab[i * m + j] = 1
            g.append(tab)

        ans = 0
        for d in range(4):
            di, dj = dirs[d]
            tdi, tdj = dirs[(d + 1) % 4]
            g_turn = g[(d + 1) % 4]
            # f: same as g, but the one clockwise turn is still
            # available from each cell.
            f = array("H", bytes(2 * n * m))
            rows, cols = order(di, dj)
            for i in rows:
                for j in cols:
                    v = grid[i][j]
                    if v != 0 and v != 2:
                        continue
                    nxt = 0 if v == 2 else 2
                    best = 0
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == nxt:
                        best = f[ni * m + nj]
                    mi, mj = i + tdi, j + tdj
                    if 0 <= mi < n and 0 <= mj < m and grid[mi][mj] == nxt:
                        turned = g_turn[mi * m + mj]
                        if turned > best:
                            best = turned
                    f[i * m + j] = 1 + best
            # Start from every 1 and step into direction d.
            for i in range(n):
                for j in range(m):
                    if grid[i][j] != 1:
                        continue
                    ni, nj = i + di, j + dj
                    length = 1
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 2:
                        length += f[ni * m + nj]
                    if length > ans:
                        ans = length
        return ans
