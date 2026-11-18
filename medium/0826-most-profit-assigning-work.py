# LeetCode 826. Most Profit Assigning Work — Medium
# https://leetcode.com/problems/most-profit-assigning-work/
# Submission 2198948906 — Accepted, Python3
#
# My thinking: I sort the jobs by difficulty and
# remember the best profit available up to each
# one. Each worker then takes the best job they
# are strong enough for, found with a binary
# search.

import bisect
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        difficulties = []
        best_profits = []
        best = 0
        for difficulty_level, value in jobs:
            best = max(best, value)
            difficulties.append(difficulty_level)
            best_profits.append(best)
        total = 0
        for ability in worker:
            index = bisect.bisect_right(difficulties, ability) - 1
            if index >= 0:
                total += best_profits[index]
        return total
