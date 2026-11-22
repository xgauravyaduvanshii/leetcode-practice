# LeetCode 1931. Painting a Grid With Three Different Colors — Hard
# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/
# Submission 2201243048 — Accepted, Python3
#
# My thinking: a column is one of a few colourings
# with no two neighbours equal, so I list them all
# and count the ways to stack compatible columns
# one after another.

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        patterns = []

        def gen(pos, cur):
            if pos == m:
                patterns.append(tuple(cur))
                return
            for c in range(3):
                if pos == 0 or cur[-1] != c:
                    cur.append(c)
                    gen(pos + 1, cur)
                    cur.pop()

        gen(0, [])
        k = len(patterns)
        compat = [[] for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if all(patterns[i][r] != patterns[j][r] for r in range(m)):
                    compat[i].append(j)
        dp = [1] * k
        for _ in range(1, n):
            ndp = [0] * k
            for i in range(k):
                ndp[i] = sum(dp[j] for j in compat[i]) % MOD
            dp = ndp
        return sum(dp) % MOD
