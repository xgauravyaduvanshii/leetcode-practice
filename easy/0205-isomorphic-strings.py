# LeetCode 205. Isomorphic Strings — Easy
# https://leetcode.com/problems/isomorphic-strings/
# Submission 2197451249 — Accepted, Python3
#
# My thinking: the mapping has to work both ways — one
# letter in s can only map to one letter in t, and one
# letter in t can only come from one letter in s. So
# I keep two dictionaries and check both directions
# as I walk through the two strings together.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        for a, b in zip(s, t):
            if a in map_s and map_s[a] != b:
                return False
            if b in map_t and map_t[b] != a:
                return False
            map_s[a] = b
            map_t[b] = a
        return True
