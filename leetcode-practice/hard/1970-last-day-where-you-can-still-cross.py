# LeetCode 1970. Last Day Where You Can Still Cross — Hard
# https://leetcode.com/problems/last-day-where-you-can-still-cross/
# Submission 2201276206 — Accepted, Python3
#
# My thinking: crossing gets only harder as cells
# flood, so I binary search the last day that still
# works — each check is just a walk from the top
# row to the bottom row over the dry cells.

from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        def can_cross(day):
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1
            q = deque()
            seen = [[False] * col for _ in range(row)]
            for c in range(col):
                if grid[0][c] == 0:
                    q.append((0, c))
                    seen[0][c] = True
            while q:
                r, c = q.popleft()
                if r == row - 1:
                    return True
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and not seen[nr][nc] and grid[nr][nc] == 0:
                        seen[nr][nc] = True
                        q.append((nr, nc))
            return False

        lo, hi = 0, len(cells)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_cross(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
