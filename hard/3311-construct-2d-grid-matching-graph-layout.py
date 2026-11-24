# LeetCode 3311. Construct 2D Grid Matching Graph Layout — Hard
# https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/
# Submission 2202318203 — Accepted, Python3
from typing import List


class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # My thinking: a grid's corners have degree 2, so I start from one. I
        # walk the top edge from the corner: at a degree-3 edge node the next
        # node along the edge is the neighbour that is NOT adjacent to the node
        # below the previous node, and the other neighbour is the node below.
        # The same walk down the left edge gives the first column. Then every
        # interior cell is the common neighbour of the cell above it and the
        # cell to its left, other than the diagonal cell. A graph whose degrees
        # are all at most 2 is a single row (or a 2x2 cycle, handled below).
        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        deg = [len(a) for a in adj]

        if max(deg) <= 2:
            start = next((i for i in range(n) if deg[i] == 1), None)
            if start is None:
                # A 2x2 grid: a 4-cycle. Lay it out as two rows of two.
                # Stop when the walk returns to the start node.
                cycle = [0]
                prev, cur = -1, 0
                while True:
                    nxt = [w for w in adj[cur] if w != prev]
                    if not nxt or nxt[0] == 0:
                        break
                    prev, cur = cur, nxt[0]
                    cycle.append(cur)
                return [[cycle[0], cycle[1]], [cycle[3], cycle[2]]]
            row = [start]
            prev, cur = -1, start
            while True:
                nxt = [w for w in adj[cur] if w != prev]
                if not nxt:
                    break
                prev, cur = cur, nxt[0]
                row.append(cur)
            return [row]

        corner = next(i for i in range(n) if deg[i] == 2)
        nb = list(adj[corner])

        def walk_first(start: int, first_step: int, other: int):
            # Walk one side of the grid from the corner; returns the side as a
            # list and, for each node on it, the node just inside the grid.
            line = [start, first_step]
            inside = {start: other}
            prev, cur = start, first_step
            while True:
                if deg[cur] == 2:
                    inside[cur] = next(w for w in adj[cur] if w != prev)
                    break
                cands = [w for w in adj[cur] if w != prev]
                # The inside neighbour is adjacent to the inside node of prev;
                # the other candidate continues along the side.
                down_node = next(w for w in cands if w in adj[inside[prev]])
                next_node = next(w for w in cands if w != down_node)
                inside[cur] = down_node
                line.append(next_node)
                prev, cur = cur, next_node
            return line, inside

        first_row, _ = walk_first(corner, nb[0], nb[1])
        first_col, _ = walk_first(corner, nb[1], nb[0])
        rows, cols = len(first_col), len(first_row)
        grid = [[-1] * cols for _ in range(rows)]
        for c, v in enumerate(first_row):
            grid[0][c] = v
        for r, v in enumerate(first_col):
            grid[r][0] = v
        for r in range(1, rows):
            for c in range(1, cols):
                common = adj[grid[r - 1][c]] & adj[grid[r][c - 1]]
                common.discard(grid[r - 1][c - 1])
                grid[r][c] = next(iter(common))
        return grid
