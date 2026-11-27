from collections import deque


class Solution:
    def isEscapePossible(self, blocked: list[list[int]], source: list[int], target: list[int]) -> bool:
        # My thinking: 200 blocked cells can fence off at most
        # 19900 cells, so a search that escapes past that many
        # cells is out in the open — check both ends that way.
        blocked_set = {(r, c) for r, c in blocked}

        def can_reach(start, goal):
            seen = {tuple(start)}
            queue = deque([tuple(start)])
            while queue:
                r, c = queue.popleft()
                if (r, c) == tuple(goal):
                    return True
                if len(seen) > 20000:
                    return True
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < 10 ** 6 and 0 <= nc < 10 ** 6:
                        if (nr, nc) not in blocked_set and (nr, nc) not in seen:
                            seen.add((nr, nc))
                            queue.append((nr, nc))
            return False

        return can_reach(source, target) and can_reach(target, source)
