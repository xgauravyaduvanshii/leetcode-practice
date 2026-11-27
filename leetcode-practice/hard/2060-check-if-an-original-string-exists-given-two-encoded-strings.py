# LeetCode 2060. Check if an Original String Exists Given Two Encoded Strings — Hard
# https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/
# Submission 2201564982 — Accepted, Python3
#
# My thinking: I walk both encodings together
# keeping how far one side has run ahead — a
# digit pushes its side forward, a letter only
# fits when the sides are level or the letter
# can fill a wildcard the other side already
# offered.

from functools import lru_cache


class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        @lru_cache(maxsize=None)
        def f(i, j, diff):
            if i == len(s1) and j == len(s2):
                return diff == 0
            if i < len(s1) and s1[i].isdigit():
                d = 0
                for k in range(i, len(s1)):
                    if not s1[k].isdigit():
                        break
                    d = d * 10 + int(s1[k])
                    if f(k + 1, j, diff + d):
                        return True
                return False
            if j < len(s2) and s2[j].isdigit():
                d = 0
                for k in range(j, len(s2)):
                    if not s2[k].isdigit():
                        break
                    d = d * 10 + int(s2[k])
                    if f(i, k + 1, diff - d):
                        return True
                return False
            if diff > 0:
                # s1 is ahead; s2 must catch up with a letter.
                if j < len(s2):
                    return f(i, j + 1, diff - 1)
                return False
            if diff < 0:
                # s2 is ahead; s1 must catch up with a letter.
                if i < len(s1):
                    return f(i + 1, j, diff + 1)
                return False
            if i < len(s1) and j < len(s2):
                return s1[i] == s2[j] and f(i + 1, j + 1, 0)
            return False

        return f(0, 0, 0)
