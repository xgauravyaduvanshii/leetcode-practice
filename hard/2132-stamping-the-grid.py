# LeetCode 2132. Stamping the Grid — Hard
# https://leetcode.com/problems/stamping-the-grid/
# Submission 2201582568 — Accepted, Python3
#
# My thinking: a stamp only lands where its
# whole footprint is empty, so I add up the
# grid to test every landing, then paint all
# the landings at once and see whether every
# empty cell got covered.

class Solution:
    def possibleToStamp(self, grid: list[list[int]], stampHeight: int, stampWidth: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        if stampHeight > m or stampWidth > n:
            return all(cell == 1 for row in grid for cell in row)
        # prefix[i+1][j+1]: occupied cells in the top-left i x j corner.
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += grid[i][j]
                prefix[i + 1][j + 1] = prefix[i][j + 1] + row_sum

        def region_sum(r1, c1, r2, c2):
            return prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1]

        diff = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - stampHeight + 1):
            for j in range(n - stampWidth + 1):
                if region_sum(i, j, i + stampHeight, j + stampWidth) == 0:
                    diff[i][j] += 1
                    diff[i + stampHeight][j] -= 1
                    diff[i][j + stampWidth] -= 1
                    diff[i + stampHeight][j + stampWidth] += 1
        # cover[i+1][j+1]: how many landings cover cell (i, j).
        cover = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                cover[i + 1][j + 1] = (
                    diff[i][j] + cover[i][j + 1] + cover[i + 1][j] - cover[i][j]
                )
                if grid[i][j] == 0 and cover[i + 1][j + 1] == 0:
                    return False
        return True
