# LeetCode 3966. Count Good Integers in a Range — Hard
# https://leetcode.com/problems/count-good-integers-in-a-range/
# Submission 2203487824 — Accepted, Python3
from functools import lru_cache


class Solution:
    def goodIntegers(self, l: int, r: int, k: int) -> int:
        # My thinking: count the good numbers up to x with
        # a digit DP and answer F(r) - F(l - 1). The DP
        # walks the digits of x tracking whether the prefix
        # is already tight, whether any digit has started,
        # and the previous digit; a new digit is allowed
        # only when it is within k of the previous one.
        # Leading zeros do not start the number, so a
        # one-digit number is always good. There are at most
        # 16 digits, so the memoised states are tiny.
        def count_upto(x: int) -> int:
            if x <= 0:
                return 0
            digits = [int(c) for c in str(x)]

            @lru_cache(maxsize=None)
            def dfs(pos: int, prev: int, tight: bool, started: bool) -> int:
                if pos == len(digits):
                    return 1 if started else 0
                limit = digits[pos] if tight else 9
                total = 0
                for d in range(limit + 1):
                    if not started and d == 0:
                        total += dfs(pos + 1, -1, tight and d == limit, False)
                    elif not started or abs(d - prev) <= k:
                        total += dfs(pos + 1, d, tight and d == limit, True)
                return total

            return dfs(0, -1, True, False)

        return count_upto(r) - count_upto(l - 1)
