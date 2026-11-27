# LeetCode 2279. Maximum Bags With Full Capacity of Rocks — Medium
# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
# Submission 2204626757 — Accepted, Python3
#
# My thinking: each bag needs capacity minus rocks more rocks to become
# full. Sort those needs from smallest to largest and fill bags in that
# order with the extra rocks — filling the cheapest bags first maximises
# how many become full, since every full bag counts the same.
class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        needs = sorted(c - r for c, r in zip(capacity, rocks))
        ans = 0
        for need in needs:
            if additionalRocks >= need:
                additionalRocks -= need
                ans += 1
            else:
                break
        return ans
