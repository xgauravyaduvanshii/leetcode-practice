# LeetCode 2999. Count the Number of Powerful Integers — Hard
# https://leetcode.com/problems/count-the-number-of-powerful-integers/
# Submission 2201853025 — Accepted, Python3
#
# My thinking: I count the powerful
# numbers up to a bound with a digit
# DP — the first digits may be anything
# up to the limit, the last ones must
# spell out s — then I take the count
# up to finish minus the count below
# start.

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        return self._count(finish, limit, s) - self._count(start - 1, limit, s)

    def _count(self, x: int, limit: int, s: str) -> int:
        if x <= 0:
            return 0
        digits = str(x)
        n, m = len(digits), len(s)
        if n < m:
            return 0
        # Powerful numbers shorter than x: any valid prefix of the
        # right length, then s. A one-digit prefix has `limit` choices
        # (1..limit); longer ones have limit * (limit + 1) ** (len - 1).
        total = 0
        for length in range(m, n):
            plen = length - m
            if plen == 0:
                total += 1
            else:
                total += limit * (limit + 1) ** (plen - 1)
        # Powerful numbers with exactly n digits: walk the digits of x
        # keeping a tight flag. Free positions take 0..limit (the first
        # one 1..limit); the last m positions must match s exactly.
        dp_tight, dp_loose = 1, 0
        for pos in range(n):
            hi = int(digits[pos])
            ndp_tight, ndp_loose = 0, 0
            if pos < n - m:
                lo_d = 1 if pos == 0 else 0
                for d in range(lo_d, limit + 1):
                    if d < hi:
                        ndp_loose += dp_tight
                    elif d == hi:
                        ndp_tight += dp_tight
                ndp_loose += dp_loose * (limit + 1 - lo_d)
            else:
                d = int(s[pos - (n - m)])
                if d < hi:
                    ndp_loose += dp_tight
                elif d == hi:
                    ndp_tight += dp_tight
                ndp_loose += dp_loose
            dp_tight, dp_loose = ndp_tight, ndp_loose
        return total + dp_tight + dp_loose
