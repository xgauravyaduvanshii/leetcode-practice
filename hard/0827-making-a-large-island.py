# LeetCode 827. Making A Large Island — Hard
# https://leetcode.com/problems/making-a-large-island/
# Submission 2198679473 — Accepted, Python3
#
# My thinking: first I label every island with its
# own number and remember its size. Then for each
# water cell I look at the distinct islands touching
# it — flipping that one cell joins them all into a
# single island, and the best flip is the answer.

from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        sizes = {}
        label = 2

        def flood(r, c, tag):
            stack = [(r, c)]
            grid[r][c] = tag
            size = 0
            while stack:
                cr, cc = stack.pop()
                size += 1
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = tag
                        stack.append((nr, nc))
            return size

        best = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    sizes[label] = flood(r, c, label)
                    best = max(best, sizes[label])
                    label += 1
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    nearby = set()
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            nearby.add(grid[nr][nc])
                    best = max(best, 1 + sum(sizes[t] for t in nearby))
        return best
