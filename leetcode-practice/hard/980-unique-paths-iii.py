class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        # My thinking: walk every empty square exactly once from the
        # start to the end — backtrack, marking squares as I go.
        rows, cols = len(grid), len(grid[0])
        empty = 0
        start = None
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    empty += 1
                elif grid[r][c] == 1:
                    start = (r, c)
        count = 0

        def dfs(r, c, remaining):
            nonlocal count
            if grid[r][c] == 2:
                if remaining == 0:
                    count += 1
                return
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] in (0, 2):
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = -1
                        dfs(nr, nc, remaining - 1)
                        grid[nr][nc] = 0
                    else:
                        dfs(nr, nc, remaining)

        grid[start[0]][start[1]] = -1
        dfs(start[0], start[1], empty)
        return count
