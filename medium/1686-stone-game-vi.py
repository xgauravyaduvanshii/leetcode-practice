# LeetCode 1686. Stone Game VI — Medium
# https://leetcode.com/problems/stone-game-vi/
# Submission 2199910067 — Accepted, Python3
#
# My thinking: taking a stone gives me its
# value and denies the other player theirs.
# Both players grab the stones with the
# biggest combined value first, so I sort by
# that sum and let them take turns.

from typing import List


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        order = sorted(range(len(aliceValues)), key=lambda i: aliceValues[i] + bobValues[i], reverse=True)
        alice = 0
        bob = 0
        for turn, i in enumerate(order):
            if turn % 2 == 0:
                alice += aliceValues[i]
            else:
                bob += bobValues[i]
        if alice > bob:
            return 1
        if alice < bob:
            return -1
        return 0
