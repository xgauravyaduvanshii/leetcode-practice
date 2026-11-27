from collections import deque


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        # My thinking: walking with the arrow is free, walking
        # against it costs one change — so a 0-1 breadth-first
        # search finds the cheapest route to the far corner.
        rows, cols = len(grid), len(grid[0])
        INF = float("inf")
        dist = [[INF] * cols for _ in range(rows)]
        dist[0][0] = 0
        queue = deque([(0, 0)])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            r, c = queue.popleft()
            for d, (dr, dc) in enumerate(dirs, start=1):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    cost = dist[r][c] + (0 if grid[r][c] == d else 1)
                    if cost < dist[nr][nc]:
                        dist[nr][nc] = cost
                        if grid[r][c] == d:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
        return dist[rows - 1][cols - 1]
