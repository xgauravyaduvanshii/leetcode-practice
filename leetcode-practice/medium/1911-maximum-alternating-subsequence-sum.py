# LeetCode 1911. Maximum Alternating Subsequence Sum — Medium
# https://leetcode.com/problems/maximum-alternating-subsequence-sum/
# Submission 2201561774 — Accepted, Python3
#
# My thinking: I keep two running bests — one
# for a run ending on a plus, one for a run
# ending on a minus — and every number either
# extends the opposite run or gets skipped.

class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        odd = 0
        even = 0
        for x in nums:
            odd, even = max(odd, even + x), max(even, odd - x)
        return odd
