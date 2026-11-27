# LeetCode 1033. Moving Stones Until Consecutive — Medium
# https://leetcode.com/problems/moving-stones-until-consecutive/
# Submission 2198989882 — Accepted, Python3
#
# My thinking: the maximum moves are just the
# empty spaces between the outer stones. For the
# minimum, the stones are already done if they
# are consecutive, one move if a pair is nearly
# together, and two moves otherwise.

from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x, y, z = sorted([a, b, c])
        if z - x == 2:
            min_moves = 0
        elif y - x <= 2 or z - y <= 2:
            min_moves = 1
        else:
            min_moves = 2
        return [min_moves, z - x - 2]
