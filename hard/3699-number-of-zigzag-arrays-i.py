# LeetCode 3699. Number of ZigZag Arrays I — Hard
# https://leetcode.com/problems/number-of-zigzag-arrays-i/
# Submission 2203047569 — Accepted, Python3
MOD = 10 ** 9 + 7


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        # My thinking: only the direction of the last step matters.
        # For each possible last value I keep two counts: arrays
        # whose last step went up into it, and arrays whose last
        # step went down into it. An upward step may only follow
        # a downward one and vice versa, so each new count is a
        # prefix sum (for up) or a suffix sum (for down) of the
        # opposite direction's counts — no equal neighbours, and
        # three in a row can never run strictly up or down.
        m = r - l + 1
        # Length 2: up[v] counts smaller values, down[v] larger ones.
        up = [v for v in range(m)]
        down = [m - 1 - v for v in range(m)]
        for _ in range(3, n + 1):
            new_up = [0] * m
            new_down = [0] * m
            s = 0
            for v in range(m):
                new_up[v] = s
                s = (s + down[v]) % MOD
            s = 0
            for v in range(m - 1, -1, -1):
                new_down[v] = s
                s = (s + up[v]) % MOD
            up, down = new_up, new_down
        return sum(up[v] + down[v] for v in range(m)) % MOD
