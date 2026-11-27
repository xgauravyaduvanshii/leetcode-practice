# LeetCode 1728. Cat and Mouse II — Hard
# https://leetcode.com/problems/cat-and-mouse-ii/
# Submission 2201119936 — Accepted, Python3
#
# My thinking: I treat every mouse/cat/turn combination
# as a game state and work backwards from the states
# where someone has already won — a state is won for
# the mouse if the mouse can move to a won state, or
# if every cat move from it is won; states nobody
# claims are draws, and a draw is not a mouse win.

from collections import deque

class Solution:
    def canMouseWin(self, grid: list[str], catJump: int, mouseJump: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        n = rows * cols
        mouse = cat = food = -1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'M':
                    mouse = r * cols + c
                elif grid[r][c] == 'C':
                    cat = r * cols + c
                elif grid[r][c] == 'F':
                    food = r * cols + c
        def moves(pos, jump):
            r, c = divmod(pos, cols)
            out = [pos]
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                for step in range(1, jump + 1):
                    nr, nc = r + dr * step, c + dc * step
                    if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] == '#':
                        break
                    out.append(nr * cols + nc)
            return out
        mouse_moves = [moves(i, mouseJump) for i in range(n)]
        cat_moves = [moves(i, catJump) for i in range(n)]
        # result[m][c][turn]: 0 unknown, 1 mouse wins, 2 cat wins
        result = [[[0, 0] for _ in range(n)] for _ in range(n)]
        degree = [[[0, 0] for _ in range(n)] for _ in range(n)]
        queue = deque()
        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(mouse_moves[m])
                degree[m][c][1] = len(cat_moves[c])
                if m == food:
                    result[m][c][0] = result[m][c][1] = 1
                    queue.append((m, c, 0))
                    queue.append((m, c, 1))
                elif c == food or m == c:
                    result[m][c][0] = result[m][c][1] = 2
                    queue.append((m, c, 0))
                    queue.append((m, c, 1))
        while queue:
            m, c, turn = queue.popleft()
            outcome = result[m][c][turn]
            if turn == 1:
                # mouse just moved to m; predecessors are (pm, c, 0)
                for pm in range(n):
                    if result[pm][c][0] != 0 or m not in mouse_moves[pm]:
                        continue
                    if outcome == 1:
                        result[pm][c][0] = 1
                        queue.append((pm, c, 0))
                    else:
                        degree[pm][c][0] -= 1
                        if degree[pm][c][0] == 0:
                            result[pm][c][0] = 2
                            queue.append((pm, c, 0))
            else:
                # cat just moved to c; predecessors are (m, pc, 1)
                for pc in range(n):
                    if result[m][pc][1] != 0 or c not in cat_moves[pc]:
                        continue
                    if outcome == 2:
                        result[m][pc][1] = 2
                        queue.append((m, pc, 1))
                    else:
                        degree[m][pc][1] -= 1
                        if degree[m][pc][1] == 0:
                            result[m][pc][1] = 1
                            queue.append((m, pc, 1))
        return result[mouse][cat][0] == 1
