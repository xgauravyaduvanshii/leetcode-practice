# LeetCode 2427. Number of Common Factors — Easy
# https://leetcode.com/problems/number-of-common-factors/
# Submission 2197782421 — Accepted, Python3
#
# My thinking: a common factor divides both numbers.
# I check every number up to the smaller of the two
# and count the ones that divide both evenly.

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return sum(1 for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0)
