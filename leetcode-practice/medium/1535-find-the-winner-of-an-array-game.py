# LeetCode 1535. Find the Winner of an Array Game — Medium
# https://leetcode.com/problems/find-the-winner-of-an-array-game/
# Submission 2199870687 — Accepted, Python3
#
# My thinking: the current champion only
# changes when a bigger number shows up. I
# count its wins as I walk the array, and stop
# the moment it reaches k.

from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        current = arr[0]
        wins = 0
        for value in arr[1:]:
            if value > current:
                current = value
                wins = 1
            else:
                wins += 1
            if wins == k:
                return current
        return current
