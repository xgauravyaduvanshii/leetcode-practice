# LeetCode 403. Frog Jump — Hard
# https://leetcode.com/problems/frog-jump/
# Submission 2198656836 — Accepted, Python3
#
# My thinking: for every stone I keep the jump sizes
# that can land on it. From a stone I try k-1, k and
# k+1, and record those sizes on the stone I land on.
# If the last stone ever gets a jump size, I can cross.

from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        reachable = {stone: set() for stone in stones}
        reachable[stones[0]].add(0)
        for stone in stones:
            for jump in reachable[stone]:
                for next_jump in (jump - 1, jump, jump + 1):
                    if next_jump > 0 and stone + next_jump in reachable:
                        reachable[stone + next_jump].add(next_jump)
        return bool(reachable[stones[-1]])
