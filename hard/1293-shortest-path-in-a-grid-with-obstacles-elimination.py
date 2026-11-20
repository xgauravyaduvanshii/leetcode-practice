from collections import deque


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        # My thinking: breadth-first search over (row, column,
        # obstacles used) — the first time we reach the target
        # is the shortest walk, and using fewer eliminations
        # to reach the same cell is never worse.
        rows, cols = len(grid), len(grid[0])
        if rows == 1 and cols == 1:
            return 0
        if k >= rows + cols - 2:
            return rows + cols - 2
        queue = deque([(0, 0, 0, 0)])
        best = [[-1] * cols for _ in range(rows)]
        best[0][0] = 0
        while queue:
            r, c, used, steps = queue.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_used = used + grid[nr][nc]
                    if new_used > k:
                        continue
                    if best[nr][nc] != -1 and best[nr][nc] <= new_used:
                        continue
                    if nr == rows - 1 and nc == cols - 1:
                        return steps + 1
                    best[nr][nc] = new_used
                    queue.append((nr, nc, new_used, steps + 1))
        return -1
