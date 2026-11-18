# LeetCode 87. Scramble String — Hard
# https://leetcode.com/problems/scramble-string/
# Submission 2198383608 — Accepted, Python3
#
# My thinking: two strings can be scrambles of each
# other only when they hold the same letters. Then
# I try every split point: either the two halves
# match straight across, or they match crossed
# over — the left half of one against the right
# half of the other. I memoise the pairs I have
# already checked so the same split is never
# tried twice.

from functools import lru_cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(maxsize=None)
        def scramble(a: str, b: str) -> bool:
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False
            n = len(a)
            for i in range(1, n):
                if (scramble(a[:i], b[:i]) and scramble(a[i:], b[i:])) or \
                   (scramble(a[:i], b[n - i:]) and scramble(a[i:], b[:n - i])):
                    return True
            return False

        return scramble(s1, s2)
