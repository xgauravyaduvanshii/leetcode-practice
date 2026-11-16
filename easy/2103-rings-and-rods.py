# LeetCode 2103. Rings and Rods — Easy
# https://leetcode.com/problems/rings-and-rods/
# Submission 2197613265 — Accepted, Python3
#
# My thinking: the input comes in color-rod pairs. I
# collect the colours on each rod in a set, and a
# rod counts when its set has all three colours —
# red, green and blue.

class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for _ in range(10)]
        for i in range(0, len(rings), 2):
            rods[int(rings[i + 1])].add(rings[i])
        return sum(1 for rod in rods if len(rod) == 3)
