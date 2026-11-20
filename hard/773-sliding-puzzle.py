from collections import deque


class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        # My thinking: treat each board as a string and search
        # breadth-first from the start — the first time we reach the
        # solved layout is the fewest moves possible.
        start = "".join(str(num) for row in board for num in row)
        target = "123450"
        neighbours = {
            0: (1, 3), 1: (0, 2, 4), 2: (1, 5),
            3: (0, 4), 4: (1, 3, 5), 5: (2, 4),
        }
        queue = deque([(start, 0)])
        seen = {start}
        while queue:
            state, moves = queue.popleft()
            if state == target:
                return moves
            zero = state.index("0")
            for nb in neighbours[zero]:
                chars = list(state)
                chars[zero], chars[nb] = chars[nb], chars[zero]
                nxt = "".join(chars)
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, moves + 1))
        return -1
