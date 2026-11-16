# LeetCode 1822. Sign of the Product of an Array — Easy
# https://leetcode.com/problems/sign-of-the-product-of-an-array/
# Submission 2197599988 — Accepted, Python3
#
# My thinking: I don't need the actual product —
# just its sign. Any zero means the answer is 0,
# and every negative number flips the sign. So I
# track the sign as I go.

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        sign = 1
        for x in nums:
            if x == 0:
                return 0
            if x < 0:
                sign = -sign
        return sign
