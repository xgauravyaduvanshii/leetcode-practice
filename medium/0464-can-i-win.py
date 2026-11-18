# LeetCode 464. Can I Win — Medium
# https://leetcode.com/problems/can-i-win/
# Submission 2198809029 — Accepted, Python3
#
# My thinking: the game state is just which numbers
# are used and how much is left to reach. I try
# every unused number — taking one that reaches the
# total wins at once, and any move that leaves the
# opponent without a win wins too. Memoisation keeps
# the search small.

from functools import lru_cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False

        @lru_cache(maxsize=None)
        def can_win(used, remaining):
            for i in range(1, maxChoosableInteger + 1):
                if used >> (i - 1) & 1:
                    continue
                if i >= remaining or not can_win(
                    used | 1 << (i - 1), remaining - i
                ):
                    return True
            return False

        return can_win(0, desiredTotal)
