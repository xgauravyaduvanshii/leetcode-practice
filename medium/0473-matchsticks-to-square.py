# LeetCode 473. Matchsticks to Square — Medium
# https://leetcode.com/problems/matchsticks-to-square/
# Submission 2198817416 — Accepted, Python3
#
# My thinking: all four sides must add up to a
# quarter of the total length. I try placing each
# matchstick — longest first — onto a side that
# still fits, backtracking when I get stuck. An
# empty side is the same as any other empty side,
# so I only try the first one.

from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        side = total // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > side:
            return False
        sides = [0] * 4

        def place(index):
            if index == len(matchsticks):
                return all(s == side for s in sides)
            for i in range(4):
                if sides[i] + matchsticks[index] <= side:
                    sides[i] += matchsticks[index]
                    if place(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
                if sides[i] == 0:
                    break
            return False

        return place(0)
