# 3963. Create Grid With Exactly One Path (Easy)
# https://leetcode.com/problems/create-grid-with-exactly-one-path/
# Submission 2200092124 — Accepted, Python3
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # My thinking: I keep the whole top row open
        # and the whole last column open, and block
        # everything else. The only way through is
        # right along the top, then down the last
        # column.
        grid = []
        for i in range(m):
            row = ""
            for j in range(n):
                row += "." if i == 0 or j == n - 1 else "#"
            grid.append(row)
        return grid
