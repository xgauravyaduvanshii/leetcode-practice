# LeetCode 10. Regular Expression Matching — Hard
# https://leetcode.com/problems/regular-expression-matching/
# Submission 2198362318 — Accepted, Python3
#
# My thinking: I match the string and the pattern
# from the front, one position at a time. A '.' or
# an equal letter matches a single character. When
# the next pattern character is '*', I can either
# skip that pair entirely, or use it to eat one
# matching character and try again. I memoise the
# positions I have already checked so nothing is
# tried twice.

from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(maxsize=None)
        def match(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)
            first = i < len(s) and (p[j] == s[i] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                return match(i, j + 2) or (first and match(i + 1, j))
            return first and match(i + 1, j + 1)

        return match(0, 0)
