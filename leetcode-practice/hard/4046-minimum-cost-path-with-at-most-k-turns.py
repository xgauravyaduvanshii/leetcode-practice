# LeetCode 4046. Minimum Cost Path With At Most K Turns — Hard
# https://leetcode.com/problems/minimum-cost-path-with-at-most-k-turns/
# Submission 2203531945 — Accepted, Python3
from typing import List

import numpy as np


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        # My thinking: a path with t turns is t+1 straight
        # runs, so track cost by (cell, last direction,
        # turns used), with directions 0 up, 1 down, 2 left,
        # 3 right. Moving straight never changes the turn
        # count or the direction, so inside one turn layer
        # and one direction the moves run along a single row
        # or column in one direction — a prefix minimum:
        # the cheapest way to be at a cell moving right is
        # the grid cost plus the cheaper of continuing the
        # run from the left neighbour or turning into this
        # run at that neighbour from the layer below. Sweep
        # each direction in its own order (right
        # left-to-right, left right-to-left, down
        # top-to-bottom, up bottom-to-top), vectorised
        # across the perpendicular axis with numpy. Layer 0
        # starts at the start cell with any last direction,
        # since the first move is free; each later layer
        # turns once more. The answer is the best over all
        # layers up to k and all four last directions at the
        # target, or -1 when nothing reaches it.
        INF = 10 ** 15
        g = np.array(grid, dtype=np.int64)
        m, n = g.shape

        def layer(prev):
            cur = np.full((4, m, n), INF, dtype=np.int64)
            if prev is None:
                cur[:, 0, 0] = g[0, 0]
                tR = tL = tD = tU = np.full((m, n), INF, dtype=np.int64)
            else:
                tR = np.minimum(np.minimum(prev[0], prev[1]), prev[2])
                tL = np.minimum(np.minimum(prev[0], prev[1]), prev[3])
                tD = np.minimum(np.minimum(prev[0], prev[2]), prev[3])
                tU = np.minimum(np.minimum(prev[1], prev[2]), prev[3])
            run = cur[3, :, 0]
            for j in range(1, n):
                cur[3, :, j] = g[:, j] + np.minimum(run, tR[:, j - 1])
                run = cur[3, :, j]
            run = cur[2, :, n - 1]
            for j in range(n - 2, -1, -1):
                cur[2, :, j] = g[:, j] + np.minimum(run, tL[:, j + 1])
                run = cur[2, :, j]
            run = cur[1, 0, :]
            for i in range(1, m):
                cur[1, i, :] = g[i, :] + np.minimum(run, tD[i - 1, :])
                run = cur[1, i, :]
            run = cur[0, m - 1, :]
            for i in range(m - 2, -1, -1):
                cur[0, i, :] = g[i, :] + np.minimum(run, tU[i + 1, :])
                run = cur[0, i, :]
            if prev is None:
                cur[:, 0, 0] = g[0, 0]
            return cur

        prev = layer(None)
        ans = int(prev[:, m - 1, n - 1].min())
        for _ in range(k):
            prev = layer(prev)
            ans = min(ans, int(prev[:, m - 1, n - 1].min()))
        return ans if ans < INF // 2 else -1
