# LeetCode 1578. Minimum Time to Make Rope Colorful — Medium
# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
# Submission 2199884004 — Accepted, Python3
#
# My thinking: within each run of the same
# color, one balloon must stay and the rest
# go. I keep the slowest one to remove and
# pay the time of all the others.

from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        i = 0
        n = len(colors)
        while i < n:
            j = i
            group_max = 0
            group_sum = 0
            while j < n and colors[j] == colors[i]:
                group_sum += neededTime[j]
                group_max = max(group_max, neededTime[j])
                j += 1
            total += group_sum - group_max
            i = j
        return total
