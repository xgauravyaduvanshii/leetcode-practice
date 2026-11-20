class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        # My thinking: each row only needs the previous row's
        # smallest and second-smallest sums — the next cell
        # takes the smallest unless it sits in the same column.
        n = len(grid)
        prev = grid[0][:]
        for r in range(1, n):
            first = second = float("inf")
            first_idx = -1
            for i, val in enumerate(prev):
                if val < first:
                    second = first
                    first = val
                    first_idx = i
                elif val < second:
                    second = val
            cur = [0] * n
            for c in range(n):
                cur[c] = grid[r][c] + (second if c == first_idx else first)
            prev = cur
        return min(prev)
