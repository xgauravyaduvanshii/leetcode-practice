# LeetCode 44. Wildcard Matching — Hard
# https://leetcode.com/problems/wildcard-matching/
# Submission 2198366478 — Accepted, Python3
#
# My thinking: I walk through the string and the
# pattern together. A '?' or an equal letter matches
# one character. A '*' remembers where it was, and
# I carry on as if it matched nothing. If the match
# breaks later, I go back to that star and let it
# swallow one more character instead. Trailing stars
# at the end of the pattern match nothing at all.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        si = pi = 0
        star = -1
        retry = 0
        while si < len(s):
            if pi < len(p) and (p[pi] == "?" or p[pi] == s[si]):
                si += 1
                pi += 1
            elif pi < len(p) and p[pi] == "*":
                star = pi
                retry = si
                pi += 1
            elif star != -1:
                pi = star + 1
                retry += 1
                si = retry
            else:
                return False
        while pi < len(p) and p[pi] == "*":
            pi += 1
        return pi == len(p)
