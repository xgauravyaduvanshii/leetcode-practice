from collections import deque


class Solution:
    def cutOffTree(self, forest: list[list[int]]) -> int:
        # My thinking: cut the trees shortest first, walking between
        # them with a breadth-first search — the steps add up, and
        # any tree we cannot reach makes the whole job impossible.
        rows, cols = len(forest), len(forest[0])
        trees = sorted((forest[r][c], r, c)
                       for r in range(rows) for c in range(cols) if forest[r][c] > 1)

        def bfs(sr, sc, tr, tc):
            queue = deque([(sr, sc, 0)])
            seen = {(sr, sc)}
            while queue:
                r, c, steps = queue.popleft()
                if r == tr and c == tc:
                    return steps
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols
                            and forest[nr][nc] != 0 and (nr, nc) not in seen):
                        seen.add((nr, nc))
                        queue.append((nr, nc, steps + 1))
            return -1

        total = 0
        r, c = 0, 0
        for _, tr, tc in trees:
            steps = bfs(r, c, tr, tc)
            if steps == -1:
                return -1
            total += steps
            r, c = tr, tc
        return total
