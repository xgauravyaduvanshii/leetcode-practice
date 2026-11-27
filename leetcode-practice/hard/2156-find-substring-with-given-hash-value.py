# LeetCode 2156. Find Substring With Given Hash Value — Hard
# https://leetcode.com/problems/find-substring-with-given-hash-value/
# Submission 2201591823 — Accepted, Python3
#
# My thinking: the hash reads the substring
# left to right with rising powers, so sliding
# it one step left means dropping the far
# letter, shifting everything up a power, and
# adding the new first letter — and sweeping
# from the right keeps the smallest index that
# matches.

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        val = lambda c: ord(c) - ord('a') + 1
        pk = pow(power, k, modulo)
        h = 0
        for i in range(n - k, n):
            h = (h + val(s[i]) * pow(power, i - (n - k), modulo)) % modulo
        ans = n - k if h == hashValue else -1
        for i in range(n - k - 1, -1, -1):
            h = (val(s[i]) + power * h - val(s[i + k]) * pk) % modulo
            if h == hashValue:
                ans = i
        return s[ans:ans + k]
