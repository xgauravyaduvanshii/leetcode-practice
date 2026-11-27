class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        # My thinking: an island already in pieces needs no
        # days; otherwise look for one cell whose removal
        # breaks it — if none exists, two days always do it.
        m, n = len(grid), len(grid[0])

        def islands(g):
            seen = [[False] * n for _ in range(m)]
            count = 0
            for i in range(m):
                for j in range(n):
                    if g[i][j] == 1 and not seen[i][j]:
                        count += 1
                        stack = [(i, j)]
                        seen[i][j] = True
                        while stack:
                            x, y = stack.pop()
                            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < m and 0 <= ny < n and g[nx][ny] == 1 and not seen[nx][ny]:
                                    seen[nx][ny] = True
                                    stack.append((nx, ny))
            return count

        if islands(grid) != 1:
            return 0
        land = sum(sum(row) for row in grid)
        if land <= 2:
            return land
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if islands(grid) != 1:
                        return 1
                    grid[i][j] = 1
        return 2
