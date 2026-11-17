# LeetCode 2441. Largest Positive Integer That Exists With Its Negative — Easy
# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
# Submission 2197785835 — Accepted, Python3
#
# My thinking: I put the numbers in a set and look
# for the biggest positive number whose negative
# also appears. If none does, the answer is -1.

class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        s = set(nums)
        best = -1
        for x in s:
            if x > 0 and -x in s:
                best = max(best, x)
        return best
