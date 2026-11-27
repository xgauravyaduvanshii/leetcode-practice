# LeetCode 2144. Minimum Cost of Buying Candies With Discount — Easy
# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
# Submission 2197614775 — Accepted, Python3
#
# My thinking: every third candy is free, so I want
# the free ones to be the cheapest ones. I sort the
# prices from most to least expensive and pay for
# every candy except every third one.

class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        return sum(c for i, c in enumerate(cost) if i % 3 != 2)
