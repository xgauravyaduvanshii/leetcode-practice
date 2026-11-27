# LeetCode 739. Daily Temperatures — Medium
# https://leetcode.com/problems/daily-temperatures/
# Submission 2198924725 — Accepted, Python3
#
# My thinking: I keep the days still waiting for
# a warmer one on a stack. When a warmer day
# arrives, it answers every cooler day below it
# in one go.

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
        return result
