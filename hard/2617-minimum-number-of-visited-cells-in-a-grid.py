# LeetCode 2617. Minimum Number of Visited Cells in a Grid — Hard
# https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/
# Submission 2201854064 — Accepted, Python3
#
# My thinking: from any cell I can jump
# to every cell still standing in its
# row or column within reach, so I keep
# each row and column as a chain that
# always points at the next unvisited
# cell — every cell is swept up once,
# and the first time the corner is
# reached the count is the smallest.

from collections import deque


class Solution:
    def minimumVisitedCells(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 1
        # row_parent[i][c]: next unvisited column >= c in row i
        row_parent = [list(range(n + 1)) for _ in range(m)]
        # col_parent[j][r]: next unvisited row >= r in column j
        col_parent = [list(range(m + 1)) for _ in range(n)]

        def find(par, x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x

        def remove(r, c):
            row_parent[r][c] = find(row_parent[r], c + 1)
            col_parent[c][r] = find(col_parent[c], r + 1)

        dist = [[-1] * n for _ in range(m)]
        dist[0][0] = 1
        remove(0, 0)
        q = deque([(0, 0)])
        while q:
            r, c = q.popleft()
            d = dist[r][c]
            # jump right along row r
            reach = min(n - 1, grid[r][c] + c)
            nc = find(row_parent[r], c + 1)
            while nc <= reach:
                dist[r][nc] = d + 1
                if r == m - 1 and nc == n - 1:
                    return d + 1
                q.append((r, nc))
                remove(r, nc)
                nc = find(row_parent[r], nc)
            # jump down along column c
            reach = min(m - 1, grid[r][c] + r)
            nr = find(col_parent[c], r + 1)
            while nr <= reach:
                dist[nr][c] = d + 1
                if nr == m - 1 and c == n - 1:
                    return d + 1
                q.append((nr, c))
                remove(nr, c)
                nr = find(col_parent[c], nr)
        return -1
