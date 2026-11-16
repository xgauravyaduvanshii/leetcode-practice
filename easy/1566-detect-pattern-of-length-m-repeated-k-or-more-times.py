# LeetCode 1566. Detect Pattern of Length M Repeated K or More Times — Easy
# https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/
# Submission 2197586186 — Accepted, Python3
#
# My thinking: I try every possible starting point.
# The pattern is the m numbers starting there, and
# it counts if the next m * k numbers are exactly
# that pattern repeated k times.

class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n - m * k + 1):
            pattern = arr[i:i + m]
            if arr[i:i + m * k] == pattern * k:
                return True
        return False
