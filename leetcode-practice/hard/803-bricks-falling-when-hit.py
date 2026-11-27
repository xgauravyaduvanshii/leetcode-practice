class Solution:
    def hitBricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        # My thinking: work backwards — take all the hit bricks away
        # first, then put them back one at a time; each brick that
        # reconnects to the roof through the restored brick is one
        # that would have fallen.
        rows, cols = len(grid), len(grid[0])
        grid = [row[:] for row in grid]
        hit_set = set()
        for r, c in hits:
            if grid[r][c] == 1:
                grid[r][c] = 0
                hit_set.add((r, c))
        parent = list(range(rows * cols + 1))
        size = [1] * (rows * cols + 1)
        ROOF = rows * cols

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        def idx(r, c):
            return r * cols + c

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                if r == 0:
                    union(idx(r, c), ROOF)
                if r > 0 and grid[r - 1][c] == 1:
                    union(idx(r, c), idx(r - 1, c))
                if c > 0 and grid[r][c - 1] == 1:
                    union(idx(r, c), idx(r, c - 1))
        answer = []
        for r, c in reversed(hits):
            if (r, c) not in hit_set:
                answer.append(0)
                continue
            grid[r][c] = 1
            before = size[find(ROOF)]
            if r == 0:
                union(idx(r, c), ROOF)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    union(idx(r, c), idx(nr, nc))
            after = size[find(ROOF)]
            answer.append(max(0, after - before - 1))
        return answer[::-1]
