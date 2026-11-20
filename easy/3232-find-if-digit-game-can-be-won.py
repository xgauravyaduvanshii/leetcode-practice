# 3232. Find if Digit Game Can Be Won (Easy)
# https://leetcode.com/problems/find-if-digit-game-can-be-won/
# Submission 2199989029 — Accepted, Python3
from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        # My thinking: Alice picks either all the
        # single-digit numbers or all the double-digit
        # ones, and Bob gets the rest. She wins if
        # either choice leaves her with more than Bob.
        single = sum(n for n in nums if n < 10)
        double = sum(n for n in nums if n >= 10)
        return single != double
