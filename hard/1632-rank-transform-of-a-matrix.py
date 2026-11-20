from collections import defaultdict


class Solution:
    def matrixRankTransform(self, matrix: list[list[int]]) -> list[list[int]]:
        # My thinking: ranks grow with the values — so handle
        # each value on its own, join equal cells that share a
        # row or column, and give the whole group one rank.
        m, n = len(matrix), len(matrix[0])
        cells = defaultdict(list)
        for i in range(m):
            for j in range(n):
                cells[matrix[i][j]].append((i, j))
        ans = [[0] * n for _ in range(m)]
        row_max = [0] * m
        col_max = [0] * n
        for val in sorted(cells):
            group = cells[val]
            parent = {}

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            for i, j in group:
                parent[("r", i)] = ("r", i)
                parent[("c", j)] = ("c", j)
            for i, j in group:
                ri, ci = find(("r", i)), find(("c", j))
                if ri != ci:
                    parent[ri] = ci
            comps = defaultdict(list)
            for i, j in group:
                comps[find(("r", i))].append((i, j))
            for comp in comps.values():
                rank = 1
                for i, j in comp:
                    rank = max(rank, row_max[i] + 1, col_max[j] + 1)
                for i, j in comp:
                    ans[i][j] = rank
                    row_max[i] = rank
                    col_max[j] = rank
        return ans
