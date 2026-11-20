from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        # My thinking: the state is where I stand plus which keys I
        # hold, so search breadth-first over those states — the first
        # time I hold every key is the shortest walk.
        rows, cols = len(grid), len(grid[0])
        start = None
        key_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "@":
                    start = (r, c)
                elif grid[r][c].islower():
                    key_count += 1
        all_keys = (1 << key_count) - 1
        queue = deque([(start[0], start[1], 0, 0)])
        seen = {(start[0], start[1], 0)}
        while queue:
            r, c, keys, steps = queue.popleft()
            if keys == all_keys:
                return steps
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                cell = grid[nr][nc]
                if cell == "#":
                    continue
                new_keys = keys
                if cell.islower():
                    new_keys |= 1 << (ord(cell) - ord("a"))
                if cell.isupper() and not (keys & (1 << (ord(cell) - ord("A")))):
                    continue
                if (nr, nc, new_keys) not in seen:
                    seen.add((nr, nc, new_keys))
                    queue.append((nr, nc, new_keys, steps + 1))
        return -1
