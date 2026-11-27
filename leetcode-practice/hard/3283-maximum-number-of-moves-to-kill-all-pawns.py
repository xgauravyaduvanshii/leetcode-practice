# LeetCode 3283. Maximum Number of Moves to Kill All Pawns — Hard
# https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/
# Submission 2202178437 — Accepted, Python3
#
# My thinking: a knight needs a fixed number of
# moves between any two squares, so I BFS the
# 50x50 board once from each pawn and the king.
# Then it is a game: Alice moves first and
# maximises the total moves, Bob minimises it,
# so I memoise over (captured-mask, last square)
# and pick max on Alice's turns, min on Bob's.

from collections import deque
from functools import lru_cache
from typing import List


class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        n = len(positions)
        pts = [(kx, ky)] + [(x, y) for x, y in positions]
        m = n + 1
        dist = [[0] * m for _ in range(m)]
        dirs = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        for s in range(m):
            d = [[-1] * 50 for _ in range(50)]
            sx, sy = pts[s]
            d[sx][sy] = 0
            q = deque([(sx, sy)])
            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 50 and 0 <= ny < 50 and d[nx][ny] == -1:
                        d[nx][ny] = d[x][y] + 1
                        q.append((nx, ny))
            for t in range(m):
                tx, ty = pts[t]
                dist[s][t] = d[tx][ty]
        full = (1 << n) - 1

        @lru_cache(maxsize=None)
        def dp(mask: int, last: int) -> int:
            if mask == full:
                return 0
            alice = (bin(mask).count("1") % 2 == 0)
            best = -10 ** 9 if alice else 10 ** 9
            for i in range(n):
                if not (mask >> i) & 1:
                    val = dist[last][i + 1] + dp(mask | (1 << i), i + 1)
                    if alice:
                        if val > best:
                            best = val
                    elif val < best:
                        best = val
            return best

        return dp(0, 0)
