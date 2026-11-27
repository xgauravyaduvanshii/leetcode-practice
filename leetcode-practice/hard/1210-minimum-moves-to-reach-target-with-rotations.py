from collections import deque


class Solution:
    def minimumMoves(self, grid: list[list[int]]) -> int:
        # My thinking: the snake is a tail cell plus a direction
        # — breadth-first search over those states, with the
        # rotation rules straight from the statement.
        n = len(grid)
        target = (n - 1, n - 2, 0)
        queue = deque([(0, 0, 0, 0)])
        seen = {(0, 0, 0)}
        while queue:
            r, c, orient, moves = queue.popleft()
            if (r, c, orient) == target:
                return moves
            if orient == 0:
                # horizontal: head at (r, c+1)
                if c + 2 < n and grid[r][c + 2] == 0:
                    self._enqueue(queue, seen, r, c + 1, 0, moves)
                if r + 1 < n and grid[r + 1][c] == 0 and grid[r + 1][c + 1] == 0:
                    self._enqueue(queue, seen, r + 1, c, 0, moves)
                    self._enqueue(queue, seen, r, c, 1, moves)
            else:
                # vertical: head at (r+1, c)
                if r + 2 < n and grid[r + 2][c] == 0:
                    self._enqueue(queue, seen, r + 1, c, 1, moves)
                if c + 1 < n and grid[r][c + 1] == 0 and grid[r + 1][c + 1] == 0:
                    self._enqueue(queue, seen, r, c + 1, 1, moves)
                    self._enqueue(queue, seen, r, c, 0, moves)
        return -1

    @staticmethod
    def _enqueue(queue, seen, r, c, orient, moves):
        state = (r, c, orient)
        if state not in seen:
            seen.add(state)
            queue.append((r, c, orient, moves + 1))
