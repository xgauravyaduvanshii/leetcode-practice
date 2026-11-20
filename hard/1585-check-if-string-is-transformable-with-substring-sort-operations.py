from collections import deque


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        # My thinking: sorting can only move a digit left past
        # bigger digits, never past a smaller one — so each
        # digit in t must come before any smaller digit still
        # waiting in s.
        pos = [deque() for _ in range(10)]
        for i, c in enumerate(s):
            pos[int(c)].append(i)
        for c in t:
            d = int(c)
            if not pos[d]:
                return False
            p = pos[d].popleft()
            for smaller in range(d):
                if pos[smaller] and pos[smaller][0] < p:
                    return False
        return True
