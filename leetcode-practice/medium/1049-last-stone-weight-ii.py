# LeetCode 1049. Last Stone Weight II — Medium
# https://leetcode.com/problems/last-stone-weight-ii/
# Submission 2198993406 — Accepted, Python3
#
# My thinking: smashing stones is the same as
# splitting them into two piles — the last stone
# is the difference between the piles. I find
# every reachable pile total and take the one
# closest to half the weight.

from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        reachable = {0}
        for stone in stones:
            reachable |= {s + stone for s in reachable}
        return total - 2 * max(s for s in reachable if s <= total // 2)
