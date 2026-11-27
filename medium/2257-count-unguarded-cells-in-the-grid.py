# LeetCode 2257. Count Unguarded Cells in the Grid — Medium
# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
# Submission 2204518544 — Accepted, Python3
#
# My thinking: a guard watches in four directions until a wall or
# another guard stops the view. I mark guards and walls on the grid,
# then sweep each row left-to-right and right-to-left and each column
# top-to-bottom and bottom-to-top, marking every empty cell a guard's
# view reaches. The answer is the empty cells never marked.
class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2
        guarded = [[False] * n for _ in range(m)]
        for i in range(m):
            seen = False
            for j in range(n):
                if grid[i][j] == 1:
                    seen = True
                elif grid[i][j] == 2:
                    seen = False
                elif seen:
                    guarded[i][j] = True
            seen = False
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    seen = True
                elif grid[i][j] == 2:
                    seen = False
                elif seen:
                    guarded[i][j] = True
        for j in range(n):
            seen = False
            for i in range(m):
                if grid[i][j] == 1:
                    seen = True
                elif grid[i][j] == 2:
                    seen = False
                elif seen:
                    guarded[i][j] = True
            seen = False
            for i in range(m - 1, -1, -1):
                if grid[i][j] == 1:
                    seen = True
                elif grid[i][j] == 2:
                    seen = False
                elif seen:
                    guarded[i][j] = True
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not guarded[i][j]:
                    ans += 1
        return ans
