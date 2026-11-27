# LeetCode 959. Regions Cut By Slashes — Medium
# https://leetcode.com/problems/regions-cut-by-slashes/
# Submission 2198976868 — Accepted, Python3
#
# My thinking: I split every cell into four
# triangles and join the ones that touch. A slash
# decides which triangles inside a cell join,
# and neighbouring cells join along their shared
# edges. The number of groups left is the answer.

from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        def index(r, c, k):
            return 4 * (r * n + c) + k

        for r in range(n):
            for c in range(n):
                ch = grid[r][c]
                if ch != "/":
                    union(index(r, c, 0), index(r, c, 1))
                    union(index(r, c, 2), index(r, c, 3))
                if ch != "\\":
                    union(index(r, c, 0), index(r, c, 3))
                    union(index(r, c, 1), index(r, c, 2))
                if r + 1 < n:
                    union(index(r, c, 2), index(r + 1, c, 0))
                if c + 1 < n:
                    union(index(r, c, 1), index(r, c + 1, 3))
        return len({find(i) for i in range(4 * n * n)})
