# LeetCode 1774. Closest Dessert Cost — Medium
# https://leetcode.com/problems/closest-dessert-cost/
# Submission 2199932806 — Accepted, Python3
#
# My thinking: each topping can be taken
# zero, one or two times, so I build every
# reachable topping cost once. Then I try
# each base with each topping sum and keep
# the closest to the target, preferring the
# cheaper one on a tie.

from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        possible = {0}
        for topping in toppingCosts:
            new = set()
            for cost in possible:
                new.add(cost)
                new.add(cost + topping)
                new.add(cost + 2 * topping)
            possible = new
        best = None
        for base in baseCosts:
            for extra in possible:
                total = base + extra
                if best is None or abs(total - target) < abs(best - target) or (abs(total - target) == abs(best - target) and total < best):
                    best = total
        return best
