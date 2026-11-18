# LeetCode 749. Contain Virus — Hard
# https://leetcode.com/problems/contain-virus/
# Submission 2198671560 — Accepted, Python3
#
# My thinking: each day I map every infected region
# and the healthy cells it threatens. I wall off the
# region with the biggest frontier — one wall per
# threatened cell — and mark it contained, then let
# every other region spread into its frontier. I keep
# going until no live region is left.

from typing import List


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        rows, cols = len(isInfected), len(isInfected[0])
        walls = 0

        def neighbours(r, c):
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc

        while True:
            seen = set()
            regions = []
            for r in range(rows):
                for c in range(cols):
                    if isInfected[r][c] == 1 and (r, c) not in seen:
                        cells = []
                        stack = [(r, c)]
                        seen.add((r, c))
                        frontier = set()
                        needed = 0
                        while stack:
                            cr, cc = stack.pop()
                            cells.append((cr, cc))
                            for nr, nc in neighbours(cr, cc):
                                if isInfected[nr][nc] == 1 and (nr, nc) not in seen:
                                    seen.add((nr, nc))
                                    stack.append((nr, nc))
                                elif isInfected[nr][nc] == 0:
                                    frontier.add((nr, nc))
                                    needed += 1
                        regions.append((cells, frontier, needed))
            if not regions:
                break
            regions.sort(key=lambda x: -len(x[1]))
            target_cells, _, needed = regions[0]
            walls += needed
            for r, c in target_cells:
                isInfected[r][c] = 2
            for _, frontier, _ in regions[1:]:
                for r, c in frontier:
                    isInfected[r][c] = 1
        return walls
