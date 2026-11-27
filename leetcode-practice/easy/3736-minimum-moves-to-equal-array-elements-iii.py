# 3736. Minimum Moves to Equal Array Elements III (Easy)
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/
# Submission 2200057562 — Accepted, Python3
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # My thinking: each move can only raise one
        # number by one, so every number has to climb
        # up to the biggest one. The moves needed are
        # just the gaps added together.
        top = max(nums)
        return sum(top - x for x in nums)
