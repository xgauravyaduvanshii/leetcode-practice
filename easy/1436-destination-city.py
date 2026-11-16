# LeetCode 1436. Destination City — Easy
# https://leetcode.com/problems/destination-city/
# Submission 2197578810 — Accepted, Python3
#
# My thinking: every city except the final one shows
# up as a starting point of some path. So the
# destination is the one city that is only ever a
# destination and never a starting point.

class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        origins = {a for a, _ in paths}
        for _, b in paths:
            if b not in origins:
                return b
        return ""
