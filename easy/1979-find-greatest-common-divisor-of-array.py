# LeetCode 1979. Find Greatest Common Divisor of Array — Easy
# https://leetcode.com/problems/find-greatest-common-divisor-of-array/
# Submission 2197607043 — Accepted, Python3
#
# My thinking: the answer is just the gcd of the
# smallest and largest numbers in the array, so I
# use math.gcd on min and max.

import math


class Solution:
    def findGCD(self, nums: list[int]) -> int:
        return math.gcd(min(nums), max(nums))
