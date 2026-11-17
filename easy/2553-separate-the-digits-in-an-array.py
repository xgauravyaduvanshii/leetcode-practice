# LeetCode 2553. Separate the Digits in an Array — Easy
# https://leetcode.com/problems/separate-the-digits-in-an-array/
# Submission 2197801752 — Accepted, Python3
#
# My thinking: I break each number into its digits,
# left to right, and append them all to the answer
# in order.

class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        res = []
        for x in nums:
            res.extend(int(ch) for ch in str(x))
        return res
