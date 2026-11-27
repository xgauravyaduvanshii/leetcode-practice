class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        # My thinking: the two robots walk down together, so
        # track both columns at once — each step tries all
        # nine moves and takes the cherries once if they meet.
        rows, cols = len(grid), len(grid[0])
        NEG = float("-inf")
        dp = [[NEG] * cols for _ in range(cols)]
        dp[0][cols - 1] = grid[0][0] + grid[0][cols - 1]
        for r in range(1, rows):
            new = [[NEG] * cols for _ in range(cols)]
            for c1 in range(cols):
                for c2 in range(cols):
                    if dp[c1][c2] == NEG:
                        continue
                    for d1 in (-1, 0, 1):
                        for d2 in (-1, 0, 1):
                            nc1, nc2 = c1 + d1, c2 + d2
                            if 0 <= nc1 < cols and 0 <= nc2 < cols:
                                gain = grid[r][nc1] + (grid[r][nc2] if nc2 != nc1 else 0)
                                new[nc1][nc2] = max(new[nc1][nc2], dp[c1][c2] + gain)
            dp = new
        return max(max(row) for row in dp)
