# LeetCode 1140. Stone Game II — Medium
# https://leetcode.com/problems/stone-game-ii/
# Submission 2199004653 — Accepted, Python3
#
# My thinking: from any pile I can take up to
# twice the last take, and whatever I leave is
# my opponent's best haul. I try every take and
# keep the one that leaves them the least.

from functools import lru_cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(maxsize=None)
        def best(i, m):
            if i + 2 * m >= n:
                return suffix[i]
            return max(suffix[i] - best(i + x, max(m, x)) for x in range(1, 2 * m + 1))

        return best(0, 1)
