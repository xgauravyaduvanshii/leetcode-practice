# LeetCode 165. Compare Version Numbers — Medium
# https://leetcode.com/problems/compare-version-numbers/
# Submission 2198433514 — Accepted, Python3
#
# My thinking: I split both versions on the dots
# and compare the parts as numbers, one by one —
# a part with leading zeros is just its number.
# The shorter version is padded with zeros, so
# "1.0" and "1.0.0" count as equal, and the first
# part that differs decides the answer.

from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parts1 = [int(p) for p in version1.split(".")]
        parts2 = [int(p) for p in version2.split(".")]
        for a, b in zip_longest(parts1, parts2, fillvalue=0):
            if a < b:
                return -1
            if a > b:
                return 1
        return 0
