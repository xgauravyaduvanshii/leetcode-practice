# LeetCode 3791. Number of Balanced Integers in a Range — Hard
# https://leetcode.com/problems/number-of-balanced-integers-in-a-range/
# Submission 2203180836 — Accepted, Python3
from functools import cache


class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        # My thinking: a number is balanced when the digits in
        # odd positions (from the left) sum to the same as the
        # digits in even positions, and it has at least two
        # digits. Count balanced numbers up to x with a digit DP
        # over the decimal string of x, tracking the running
        # difference (odd-position sum minus even-position sum)
        # and whether the prefix is still tight to x; a number
        # is counted when the difference ends at zero. Leading
        # zeroes only shift the positions, which flips the sign
        # of the difference but keeps zero at zero, and the
        # number 0 itself is counted once on both sides, so the
        # answer is count(high) - count(low - 1). Single-digit
        # numbers have a nonzero difference, so the two-digit
        # minimum takes care of itself.
        def count_upto(x: int) -> int:
            if x < 0:
                return 0
            s = str(x)

            @cache
            def dfs(pos: int, diff: int, tight: bool) -> int:
                if pos == len(s):
                    return 1 if diff == 0 else 0
                limit = int(s[pos]) if tight else 9
                total = 0
                for d in range(limit + 1):
                    ndiff = diff + d if pos % 2 == 0 else diff - d
                    total += dfs(pos + 1, ndiff, tight and d == limit)
                return total

            return dfs(0, 0, True)

        return count_upto(high) - count_upto(low - 1)
