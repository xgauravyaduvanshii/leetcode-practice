# LeetCode 1798. Maximum Number of Consecutive Values You Can Make — Medium
# https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/
# Submission 2199935819 — Accepted, Python3
#
# My thinking: after sorting, if I can make
# every value up to some total, a coin no
# bigger than one past that total stretches
# the range further. The first coin that is
# too big stops the run.

from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        reachable = 0
        for coin in coins:
            if coin > reachable + 1:
                break
            reachable += coin
        return reachable + 1
