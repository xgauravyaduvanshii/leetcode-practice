# LeetCode 1573. Number of Ways to Split a String — Medium
# https://leetcode.com/problems/number-of-ways-to-split-a-string/
# Submission 2199878741 — Accepted, Python3
#
# My thinking: the ones must split evenly into
# three parts. The cuts can land anywhere in
# the zero gaps between the parts, so the
# answer is the two gap sizes multiplied.

class Solution:
    def numWays(self, s: str) -> int:
        mod = 10 ** 9 + 7
        ones = s.count("1")
        if ones == 0:
            n = len(s)
            return (n - 1) * (n - 2) // 2 % mod
        if ones % 3:
            return 0
        per_part = ones // 3
        seen = 0
        first_gap = 0
        second_gap = 0
        for ch in s:
            if ch == "1":
                seen += 1
            elif seen == per_part:
                first_gap += 1
            elif seen == 2 * per_part:
                second_gap += 1
        return (first_gap + 1) * (second_gap + 1) % mod
