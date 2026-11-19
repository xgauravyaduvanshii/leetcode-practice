# LeetCode 1222. Queens That Can Attack the King — Medium
# https://leetcode.com/problems/queens-that-can-attack-the-king/
# Submission 2199013346 — Accepted, Python3
#
# My thinking: from the king I look in all
# eight directions, one square at a time. The
# first queen met in each direction can attack
# — anything behind her is blocked.

from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queen_set = {(r, c) for r, c in queens}
        result = []
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                r, c = king
                while True:
                    r += dr
                    c += dc
                    if not (0 <= r < 8 and 0 <= c < 8):
                        break
                    if (r, c) in queen_set:
                        result.append([r, c])
                        break
        return result
