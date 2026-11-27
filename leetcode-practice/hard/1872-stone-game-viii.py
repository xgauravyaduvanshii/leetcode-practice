# LeetCode 1872. Stone Game VIII — Hard
# https://leetcode.com/problems/stone-game-viii/
# Submission 2201211263 — Accepted, Python3
#
# My thinking: taking a prefix leaves the other
# player the best value of the game on what is
# left, so I walk the prefix sums from the end —
# at each point I either take everything or take
# this prefix and hand over the best value so
# far.

import itertools

class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        prefix = list(itertools.accumulate(stones))
        res = prefix[-1]
        for i in range(len(stones) - 2, 0, -1):
            res = max(res, prefix[i] - res)
        return res
