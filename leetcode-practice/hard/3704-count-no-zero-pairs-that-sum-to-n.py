# LeetCode 3704. Count No-Zero Pairs That Sum to N — Hard
# https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/
# Submission 2203054713 — Accepted, Python3


class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        # My thinking: a no-zero number has no zero digit at any
        # position below its most significant digit, so while I
        # scan the digits of n from least to most significant I
        # only need to know, for each of a and b, whether it is
        # still "active" (all its digits so far are 1..9 and it
        # may continue) or has "ended" (its higher digits are all
        # blank). The units digit of each must be 1..9 — a zero
        # there would mean the number is 0 or has an interior
        # zero. At each position I try every digit pair that fits
        # the digit of n plus the carry, and carry the rest.
        digits = [int(c) for c in str(n)][::-1]
        # dp[carry][a_active][b_active]
        dp = [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
        dp[0][1][1] = 1
        for i, d in enumerate(digits):
            ndp = [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
            for carry in (0, 1):
                for a_active in (0, 1):
                    for b_active in (0, 1):
                        cur = dp[carry][a_active][b_active]
                        if cur == 0:
                            continue
                        a_digits = self._digits(a_active, i)
                        b_digits = self._digits(b_active, i)
                        for da in a_digits:
                            for db in b_digits:
                                s = da + db + carry
                                if s % 10 != d:
                                    continue
                                na = 1 if da > 0 else 0
                                nb = 1 if db > 0 else 0
                                ndp[s // 10][na][nb] += cur
            dp = ndp
        # After the most significant digit the carry must be 0;
        # a and b may be active or ended, both are valid.
        return sum(dp[0][a][b] for a in (0, 1) for b in (0, 1))

    def _digits(self, active: int, pos: int):
        # Digits allowed at this position: an ended number only
        # contributes a blank 0; an active number takes 1..9 at
        # the units place (it must have a units digit) and 0..9
        # above it, where 0 means it ends here.
        if active == 0:
            return (0,)
        if pos == 0:
            return range(1, 10)
        return range(0, 10)
