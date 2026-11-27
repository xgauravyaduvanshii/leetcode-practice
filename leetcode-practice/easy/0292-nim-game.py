# LeetCode 292. Nim Game — Easy
# https://leetcode.com/problems/nim-game/
# Submission 2197462524 — Accepted, Python3
#
# My thinking: with 4 stones the first player always
# loses — whatever they take (1, 2 or 3), the other
# player takes the rest. The same is true for any
# multiple of 4. So the first player wins exactly
# when n is not a multiple of 4.

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
