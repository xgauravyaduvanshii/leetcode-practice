# LeetCode 983. Minimum Cost For Tickets — Medium
# https://leetcode.com/problems/minimum-cost-for-tickets/
# Submission 2198980576 — Accepted, Python3
#
# My thinking: I work out the cheapest cost for
# every day of the year. On a travel day I pick
# the cheapest of a 1-day, 7-day or 30-day pass
# covering it; on other days the cost just carries
# over.

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel = set(days)
        dp = [0] * 366
        for day in range(1, 366):
            if day not in travel:
                dp[day] = dp[day - 1]
            else:
                dp[day] = min(
                    dp[day - 1] + costs[0],
                    dp[max(0, day - 7)] + costs[1],
                    dp[max(0, day - 30)] + costs[2],
                )
        return dp[365]
