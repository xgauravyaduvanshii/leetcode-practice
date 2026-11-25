# LeetCode 3753. Total Waviness of Numbers in Range II — Hard
# https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/
# Submission 2203154518 — Accepted, Python3
from functools import lru_cache


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # My thinking: the waviness of one number is the count
        # of its interior digits that are peaks or valleys, so
        # I count it with a digit DP: walking the decimal
        # digits left to right I only need the previous two
        # digits to tell whether the middle one is a peak or a
        # valley, plus the tight flag and whether any non-zero
        # digit has started yet (leading zeros are not digits
        # of the number). The DP returns both how many numbers
        # a prefix admits and their total waviness, and the
        # answer for [num1, num2] is the prefix total at num2
        # minus the prefix total at num1 - 1.
        def total(n: int) -> int:
            if n <= 0:
                return 0
            digits = list(map(int, str(n)))

            @lru_cache(maxsize=None)
            def dfs(i: int, prev2: int, prev1: int, tight: bool, started: bool):
                if i == len(digits):
                    return (1, 0)
                limit = digits[i] if tight else 9
                count = 0
                waviness = 0
                for d in range(limit + 1):
                    ntight = tight and d == limit
                    nstarted = started or d != 0
                    if not nstarted:
                        c, w = dfs(i + 1, -1, -1, ntight, False)
                        count += c
                        waviness += w
                    else:
                        add = 0
                        if started and prev2 != -1:
                            if (prev1 > prev2 and prev1 > d) or (prev1 < prev2 and prev1 < d):
                                add = 1
                        if started:
                            nprev2, nprev1 = prev1, d
                        else:
                            nprev2, nprev1 = -1, d
                        c, w = dfs(i + 1, nprev2, nprev1, ntight, True)
                        count += c
                        waviness += w + add * c
                return (count, waviness)

            return dfs(0, -1, -1, True, False)[1]

        return total(num2) - total(num1 - 1)
