# LeetCode 2197. Replace Non-Coprime Numbers in Array — Hard
# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
# Submission 2201615559 — Accepted, Python3
#
# My thinking: neighbours that share a factor
# fuse into their lowest common multiple, and
# a fusion can wake up the pair behind it —
# so I keep a stack and fuse while the top
# two still share a factor.

import math


class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        stack = []
        for x in nums:
            stack.append(x)
            while len(stack) >= 2 and math.gcd(stack[-1], stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b // math.gcd(a, b))
        return stack
