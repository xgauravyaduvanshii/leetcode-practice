class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        # My thinking: a rhombus of "radius" d has its four
        # corners d steps up/down/left/right from the centre —
        # walk each edge and add the border cells.
        rows, cols = len(grid), len(grid[0])
        sums = set()
        for r in range(rows):
            for c in range(cols):
                sums.add(grid[r][c])
                max_d = min(r, c, rows - 1 - r, cols - 1 - c)
                for d in range(1, max_d + 1):
                    total = 0
                    for i in range(d):
                        total += grid[r - d + i][c + i]
                        total += grid[r + i][c + d - i]
                        total += grid[r + d - i][c - i]
                        total += grid[r - i][c - d + i]
                    sums.add(total)
        return sorted(sums, reverse=True)[:3]
