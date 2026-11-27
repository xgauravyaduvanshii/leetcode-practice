# LeetCode 674. Longest Continuous Increasing Subsequence — Easy
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# Submission 2197512888 — Accepted, Python3
#
# My thinking: I walk through the numbers keeping
# the length of the current increasing run. If the
# next number is bigger, the run grows by one;
# otherwise it restarts at 1. The best run I have
# seen is the answer.

class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        best = 1
        current = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current += 1
                best = max(best, current)
            else:
                current = 1
        return best
