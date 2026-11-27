# LeetCode 2344. Minimum Deletions to Make Array Divisible — Hard
# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/
# Submission 2201691005 — Accepted, Python3
#
# My thinking: the smallest survivor must
# divide every number it has to cover, so
# it must divide their gcd — I sort the
# array, take the first number that does,
# and drop everything smaller than it.

import math


class Solution:
    def minOperations(self, nums: list[int], numsDivide: list[int]) -> int:
        g = 0
        for x in numsDivide:
            g = math.gcd(g, x)
        nums.sort()
        for i, x in enumerate(nums):
            if g % x == 0:
                return i
        return -1
