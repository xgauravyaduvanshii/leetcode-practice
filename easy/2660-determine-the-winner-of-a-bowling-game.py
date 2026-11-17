# LeetCode 2660. Determine the Winner of a Bowling Game — Easy
# https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/
# Submission 2197813825 — Accepted, Python3
#
# My thinking: a throw is worth double when either
# of the previous two throws was a strike (10).
# I score both players the same way and compare
# the totals.

from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(p):
            total = 0
            for i, x in enumerate(p):
                if (i >= 1 and p[i - 1] == 10) or (i >= 2 and p[i - 2] == 10):
                    total += 2 * x
                else:
                    total += x
            return total
        s1 = score(player1)
        s2 = score(player2)
        if s1 > s2:
            return 1
        if s2 > s1:
            return 2
        return 0
