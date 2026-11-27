# LeetCode 3449. Maximize the Minimum Game Score — Hard
# https://leetcode.com/problems/maximize-the-minimum-game-score/
# Submission 2202544787 — Accepted 692/692, Python3
from typing import List


class Solution:
    def maximizeMinimumGameScore(self, points: List[int], m: int) -> int:
        # My thinking: binary-search the answer X, and check it by
        # walking left to right. Each index i needs ceil(X / points[i])
        # visits; arriving there gives one, and any shortfall is
        # topped up by bouncing to the next index and back, which
        # costs 2 moves and also gives the neighbour a visit (the
        # last index bounces left instead). Stop as soon as every
        # index has enough visits, and fail as soon as moves exceed m.
        n = len(points)

        def can(x: int) -> bool:
            need = [(x + p - 1) // p for p in points]
            visits = [0] * n
            remaining = sum(1 for v in need if v > 0)
            moves = 0

            def add(j: int, delta: int) -> None:
                nonlocal remaining
                before = visits[j]
                visits[j] += delta
                if before < need[j] <= visits[j]:
                    remaining -= 1

            for i in range(n):
                if remaining == 0:
                    break
                add(i, 1)
                moves += 1
                if moves > m:
                    return False
                if remaining == 0:
                    break
                if visits[i] < need[i]:
                    extra = need[i] - visits[i]
                    if i < n - 1:
                        add(i, extra)
                        add(i + 1, extra)
                    else:
                        add(i, extra)
                        add(i - 1, extra)
                    moves += 2 * extra
                    if moves > m:
                        return False
                if remaining == 0:
                    break
            return moves <= m

        lo, hi = 0, m * max(points)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
