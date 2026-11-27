# LeetCode 2290. Minimum Obstacle Removal to Reach Corner — Hard
# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/
# Submission 2201661633 — Accepted, Python3
#
# My thinking: stepping on an empty cell
# costs nothing and an obstacle costs one,
# so I walk the grid with a 0-1 queue and
# the first time I reach the corner I have
# paid the fewest obstacles possible.

from collections import deque


class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[-1] * n for _ in range(m)]
        dist[0][0] = 0
        dq = deque([(0, 0)])
        while dq:
            x, y = dq.popleft()
            d = dist[x][y]
            if x == m - 1 and y == n - 1:
                return d
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == -1:
                    cost = d + grid[nx][ny]
                    dist[nx][ny] = cost
                    if grid[nx][ny] == 0:
                        dq.appendleft((nx, ny))
                    else:
                        dq.append((nx, ny))
        return dist[m - 1][n - 1]
