class Solution:
    def minFlips(self, mat: list[list[int]]) -> int:
        # My thinking: the board is at most 3 by 3, so just try
        # every flip pattern and keep the smallest that clears
        # the board.
        rows, cols = len(mat), len(mat[0])
        cells = rows * cols
        best = float("inf")
        for mask in range(1 << cells):
            grid = [row[:] for row in mat]
            flips = 0
            for bit in range(cells):
                if mask & (1 << bit):
                    flips += 1
                    r, c = divmod(bit, cols)
                    for nr, nc in ((r, c), (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < rows and 0 <= nc < cols:
                            grid[nr][nc] ^= 1
            if all(grid[r][c] == 0 for r in range(rows) for c in range(cols)):
                best = min(best, flips)
        return -1 if best == float("inf") else best
