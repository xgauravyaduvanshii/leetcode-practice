# LeetCode 1561. Maximum Number of Coins You Can Get — Medium
# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
# Submission 2199877116 — Accepted, Python3
#
# My thinking: in each round of three piles I
# take the second biggest. Sorting lets me
# hand the biggest to the opponent, take the
# next one myself, and give the smallest to
# the third player.

from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        for i in range(len(piles) // 3):
            total += piles[len(piles) - 2 - 2 * i]
        return total
