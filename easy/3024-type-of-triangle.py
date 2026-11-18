# LeetCode 3024. Type of Triangle — Easy
# https://leetcode.com/problems/type-of-triangle/
# Submission 2198716346 — Accepted, Python3
#
# My thinking: I sort the sides first, so the
# triangle check is just whether the two short sides
# add up to more than the long one. Then equal sides
# decide between equilateral, isosceles and scalene.

from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)
        if a + b <= c:
            return "none"
        if a == b == c:
            return "equilateral"
        if a == b or b == c:
            return "isosceles"
        return "scalene"
