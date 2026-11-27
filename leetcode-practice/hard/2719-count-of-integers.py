# LeetCode 2719. Count of Integers — Hard
# https://leetcode.com/problems/count-of-integers/
# Submission 2201877111 — Accepted, Python3
#
# My thinking: counting numbers up to
# a bound by their digit sum is a walk
# down the digits, so I count up to the
# top of the range and subtract the
# count up to just below the bottom —
# the difference is exactly the numbers
# that live between them.

from functools import lru_cache


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10 ** 9 + 7

        def count_upto(s: str) -> int:
            digits = list(map(int, s))

            @lru_cache(maxsize=None)
            def dp(pos: int, tight: int, total: int) -> int:
                if total > max_sum:
                    return 0
                if pos == len(digits):
                    return 1 if min_sum <= total <= max_sum else 0
                limit = digits[pos] if tight else 9
                ans = 0
                for d in range(limit + 1):
                    ans += dp(pos + 1, tight and d == limit, total + d)
                return ans % MOD

            return dp(0, 1, 0)

        def minus_one(s: str) -> str:
            ds = list(map(int, s))
            i = len(ds) - 1
            while ds[i] == 0:
                ds[i] = 9
                i -= 1
            ds[i] -= 1
            t = "".join(map(str, ds)).lstrip("0")
            return t if t else "0"

        return (count_upto(num2) - count_upto(minus_one(num1))) % MOD
