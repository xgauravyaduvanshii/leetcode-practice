import math
from functools import lru_cache


class Solution:
    def getProbability(self, balls: list[int]) -> float:
        # My thinking: go colour by colour, splitting each
        # colour's balls between the two boxes — count how
        # many splits end even with the same number of
        # distinct colours on both sides.
        total = sum(balls)
        half = total // 2
        k = len(balls)

        @lru_cache(maxsize=None)
        def dp(i, in_box1, distinct1, distinct2):
            if i == k:
                return 1.0 if in_box1 == half and distinct1 == distinct2 else 0.0
            ways = 0.0
            c = balls[i]
            for x in range(c + 1):
                ways += math.comb(c, x) * dp(i + 1,
                                             in_box1 + x,
                                             distinct1 + (1 if x > 0 else 0),
                                             distinct2 + (1 if x < c else 0))
            return ways

        favourable = dp(0, 0, 0, 0)
        return favourable / math.comb(total, half)
