# 3502. Minimum Cost to Reach Every Position (Easy)
# https://leetcode.com/problems/minimum-cost-to-reach-every-position/
# Submission 2200025256 — Accepted, Python3
from typing import List


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        # My thinking: to reach any spot I can stop at
        # the cheapest spot so far, so the answer for
        # each position is just the smallest cost seen
        # up to there.
        answer = []
        best = cost[0]
        for c in cost:
            best = min(best, c)
            answer.append(best)
        return answer
