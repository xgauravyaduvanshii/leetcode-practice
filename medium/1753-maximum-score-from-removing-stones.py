# LeetCode 1753. Maximum Score From Removing Stones — Medium
# https://leetcode.com/problems/maximum-score-from-removing-stones/
# Submission 2199927841 — Accepted, Python3
#
# My thinking: every move takes two stones
# from two piles. If the biggest pile is no
# bigger than the other two together, I can
# use every stone; otherwise the two small
# piles run out first.

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        piles = sorted([a, b, c])
        if piles[0] + piles[1] <= piles[2]:
            return piles[0] + piles[1]
        return (a + b + c) // 2
