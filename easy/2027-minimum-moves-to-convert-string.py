# LeetCode 2027. Minimum Moves to Convert String — Easy
# https://leetcode.com/problems/minimum-moves-to-convert-string/
# Submission 2197609725 — Accepted, Python3
#
# My thinking: one move can flip three consecutive
# characters. So when I hit an 'X', I spend one
# move on it and the next two characters together —
# the greedy choice is always best — and skip ahead
# by three. 'O's cost nothing.

class Solution:
    def minimumMoves(self, s: str) -> int:
        moves = 0
        i = 0
        while i < len(s):
            if s[i] == 'X':
                moves += 1
                i += 3
            else:
                i += 1
        return moves
