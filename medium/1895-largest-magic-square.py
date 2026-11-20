class Solution:
    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        # My thinking: try the biggest squares first — a
        # square is magic when every row, every column and
        # both diagonals add up to the same number.
        m, n = len(grid), len(grid[0])
        row_pre = [[0] * (n + 1) for _ in range(m)]
        col_pre = [[0] * (m + 1) for _ in range(n)]
        for i in range(m):
            for j in range(n):
                row_pre[i][j + 1] = row_pre[i][j] + grid[i][j]
                col_pre[j][i + 1] = col_pre[j][i] + grid[i][j]

        def is_magic(r, c, k):
            target = row_pre[r][c + k] - row_pre[r][c]
            for i in range(r, r + k):
                if row_pre[i][c + k] - row_pre[i][c] != target:
                    return False
            for j in range(c, c + k):
                if col_pre[j][r + k] - col_pre[j][r] != target:
                    return False
            d1 = d2 = 0
            for t in range(k):
                d1 += grid[r + t][c + t]
                d2 += grid[r + t][c + k - 1 - t]
            return d1 == target and d2 == target

        for k in range(min(m, n), 0, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
        return 1
