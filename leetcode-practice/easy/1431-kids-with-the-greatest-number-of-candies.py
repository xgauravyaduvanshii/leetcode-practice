# LeetCode 1431. Kids With the Greatest Number of Candies — Easy
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Submission 2197578555 — Accepted, Python3
#
# My thinking: first I find the biggest candy count
# any kid already has. Then each kid can reach the
# top exactly when their candies plus the extra
# ones are at least that big.

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        greatest = max(candies)
        return [c + extraCandies >= greatest for c in candies]
