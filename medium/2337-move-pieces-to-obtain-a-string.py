# LeetCode 2337. Move Pieces to Obtain a String — Medium
# https://leetcode.com/problems/move-pieces-to-obtain-a-string/
# Submission 2197623661 — Accepted, Python3
#
# My thinking: blanks don't matter, so I compare the
# pieces in order — L and R must appear in the same
# order in both strings. An L can only move left and
# an R can only move right, so I check each piece
# didn't have to move the wrong way.

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s = [(ch, i) for i, ch in enumerate(start) if ch != '_']
        t = [(ch, i) for i, ch in enumerate(target) if ch != '_']
        if len(s) != len(t):
            return False
        for (c1, i), (c2, j) in zip(s, t):
            if c1 != c2:
                return False
            if c1 == 'L' and i < j:
                return False
            if c1 == 'R' and i > j:
                return False
        return True
