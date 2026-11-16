# LeetCode 1995. Count Special Quadruplets — Easy
# https://leetcode.com/problems/count-special-quadruplets/
# Submission 2197608098 — Accepted, Python3
#
# My thinking: a quadruplet is special when the
# first three numbers add up to the fourth. I try
# every combination of four positions and count the
# ones where a + b + c == d.

from itertools import combinations


class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        count = 0
        for a, b, c, d in combinations(nums, 4):
            if a + b + c == d:
                count += 1
        return count
