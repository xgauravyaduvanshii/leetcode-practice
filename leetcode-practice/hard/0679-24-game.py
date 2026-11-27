# LeetCode 679. 24 Game — Hard
# https://leetcode.com/problems/24-game/
# Submission 2198666765 — Accepted, Python3
#
# My thinking: with only four numbers I can just try
# everything — pick any two, combine them with plus,
# minus, times or divide (both orders for the last
# two), and keep going until one number is left. If
# any path lands on 24, the cards work.

from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def solve(values):
            if len(values) == 1:
                return abs(values[0] - 24) < 1e-6
            for i in range(len(values)):
                for j in range(len(values)):
                    if i == j:
                        continue
                    rest = [
                        values[t]
                        for t in range(len(values))
                        if t != i and t != j
                    ]
                    for result in (
                        values[i] + values[j],
                        values[i] - values[j],
                        values[i] * values[j],
                    ):
                        if solve(rest + [result]):
                            return True
                    if abs(values[j]) > 1e-9:
                        if solve(rest + [values[i] / values[j]]):
                            return True
            return False

        return solve([float(x) for x in cards])
