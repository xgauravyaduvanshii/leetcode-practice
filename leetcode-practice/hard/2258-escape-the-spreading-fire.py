# LeetCode 2258. Escape the Spreading Fire — Hard
# https://leetcode.com/problems/escape-the-spreading-fire/
# Submission 2201640470 — Accepted, Python3
#
# My thinking: I first time when the fire
# reaches every cell, then I binary-search
# the longest I can wait — a wait works
# when I can still outrun the fire to the
# safehouse, arriving there no later than
# the flames do.

from collections import deque


class Solution:
    def maximumMinutes(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = float('inf')
        fire = [[INF] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fire[i][j] = 0
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 2 and fire[nx][ny] == INF:
                    fire[nx][ny] = fire[x][y] + 1
                    q.append((nx, ny))

        def can(wait: int) -> bool:
            if wait >= fire[0][0]:
                return False
            dist = [[-1] * n for _ in range(m)]
            dist[0][0] = wait
            q = deque([(0, 0)])
            while q:
                x, y = q.popleft()
                t = dist[x][y]
                if x == m - 1 and y == n - 1:
                    return True
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 2 and dist[nx][ny] == -1:
                        nt = t + 1
                        if nx == m - 1 and ny == n - 1:
                            if nt <= fire[nx][ny]:
                                dist[nx][ny] = nt
                                q.append((nx, ny))
                        elif nt < fire[nx][ny]:
                            dist[nx][ny] = nt
                            q.append((nx, ny))
            return False

        if not can(0):
            return -1
        lo, hi = 0, 10 ** 9
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
