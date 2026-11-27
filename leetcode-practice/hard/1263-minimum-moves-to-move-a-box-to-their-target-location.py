from collections import deque


class Solution:
    def minPushBox(self, grid: list[list[str]]) -> int:
        # My thinking: each push moves the box one step, and the
        # player just needs a walkable path to the pushing spot —
        # an outer search over pushes with an inner walk check.
        rows, cols = len(grid), len(grid[0])
        box = player = target = None
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "B":
                    box = (r, c)
                elif grid[r][c] == "S":
                    player = (r, c)
                elif grid[r][c] == "T":
                    target = (r, c)

        def can_reach(start, goal, box_pos):
            seen = {start}
            queue = deque([start])
            while queue:
                r, c = queue.popleft()
                if (r, c) == goal:
                    return True
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] != "#" and (nr, nc) != box_pos and (nr, nc) not in seen:
                            seen.add((nr, nc))
                            queue.append((nr, nc))
            return False

        queue = deque([(box, player, 0)])
        seen = {(box, player)}
        while queue:
            box_pos, player_pos, pushes = queue.popleft()
            if box_pos == target:
                return pushes
            br, bc = box_pos
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_box = (br + dr, bc + dc)
                push_spot = (br - dr, bc - dc)
                if not (0 <= new_box[0] < rows and 0 <= new_box[1] < cols):
                    continue
                if grid[new_box[0]][new_box[1]] == "#":
                    continue
                if not (0 <= push_spot[0] < rows and 0 <= push_spot[1] < cols):
                    continue
                if grid[push_spot[0]][push_spot[1]] == "#":
                    continue
                if can_reach(player_pos, push_spot, box_pos):
                    # after the push the player stands where the box was
                    state = (new_box, box_pos)
                    if state not in seen:
                        seen.add(state)
                        queue.append((new_box, box_pos, pushes + 1))
        return -1
