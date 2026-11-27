# LeetCode 3906. Count Good Integers on a Grid Path — Hard
# https://leetcode.com/problems/count-good-integers-on-a-grid-path/
# Submission 2203374752 — Accepted, Python3
from functools import lru_cache


class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        # My thinking: pad x to 16 digits and lay it row by
        # row into a 4x4 grid. The path starts at (0, 0)
        # and takes three D steps and three R steps, so it
        # visits 7 cells whose digit positions 4*row+col
        # strictly increase along the path — the first is
        # position 0 and the last is position 15. Only the
        # digits on those 7 positions matter, and they must
        # read non-decreasing in path order; every other
        # digit is free. Count the good numbers up to X
        # with a digit DP over the 16 positions, carrying
        # the tight flag and the previous path digit (the
        # scan meets the path positions in path order, so a
        # path digit only has to be at least the previous
        # one), then answer count(r) - count(l - 1).
        row = col = 0
        path = [0]
        for ch in directions:
            if ch == 'D':
                row += 1
            else:
                col += 1
            path.append(4 * row + col)
        path_set = set(path)

        def count_upto(x):
            if x < 0:
                return 0
            s = str(x).rjust(16, '0')

            @lru_cache(maxsize=None)
            def dp(pos, tight, prev):
                if pos == 16:
                    return 1
                limit = int(s[pos]) if tight else 9
                total = 0
                on_path = pos in path_set
                for d in range(limit + 1):
                    if on_path and prev >= 0 and d < prev:
                        continue
                    total += dp(pos + 1, tight and d == limit, d if on_path else prev)
                return total

            return dp(0, True, -1)

        return count_upto(r) - count_upto(l - 1)
