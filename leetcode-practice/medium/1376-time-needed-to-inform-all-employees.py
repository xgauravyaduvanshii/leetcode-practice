# LeetCode 1376. Time Needed to Inform All Employees — Medium
# https://leetcode.com/problems/time-needed-to-inform-all-employees/
# Submission 2199043335 — Accepted, Python3
#
# My thinking: the news travels down the
# management tree, and each manager adds their
# own delay. I walk from the head down every
# chain and keep the longest total time.

from collections import defaultdict
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        reports = defaultdict(list)
        for employee, boss in enumerate(manager):
            if boss != -1:
                reports[boss].append(employee)
        best = 0
        stack = [(headID, 0)]
        while stack:
            person, time = stack.pop()
            best = max(best, time)
            for report in reports[person]:
                stack.append((report, time + informTime[person]))
        return best
