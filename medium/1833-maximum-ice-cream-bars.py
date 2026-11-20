# LeetCode 1833. Maximum Ice Cream Bars — Medium
# https://leetcode.com/problems/maximum-ice-cream-bars/
# Submission 2199945272 — Accepted, Python3
#
# My thinking: buying the cheapest bars
# first leaves the most money for the most
# bars. I sort and keep buying until the
# coins run out.

from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for cost in costs:
            if coins < cost:
                break
            coins -= cost
            count += 1
        return count
