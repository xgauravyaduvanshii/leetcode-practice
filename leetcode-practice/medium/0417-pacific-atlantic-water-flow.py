# LeetCode 417. Pacific Atlantic Water Flow — Medium
# https://leetcode.com/problems/pacific-atlantic-water-flow/
# Submission 2198785144 — Accepted, Python3
#
# My thinking: instead of asking where each cell
# drains, I start from each ocean and walk uphill —
# water can only flow down, so the cells I reach
# from an edge are exactly the ones that drain to
# that ocean. Cells reached from both oceans are
# the answer.

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        def flow(reachable, starts):
            stack = list(starts)
            while stack:
                r, c = stack.pop()
                if reachable[r][c]:
                    continue
                reachable[r][c] = True
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        stack.append((nr, nc))

        flow(pacific, [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)])
        flow(
            atlantic,
            [(r, cols - 1) for r in range(rows)]
            + [(rows - 1, c) for c in range(cols)],
        )
        return [
            [r, c]
            for r in range(rows)
            for c in range(cols)
            if pacific[r][c] and atlantic[r][c]
        ]
