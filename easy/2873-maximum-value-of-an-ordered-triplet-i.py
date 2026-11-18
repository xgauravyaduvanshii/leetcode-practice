# LeetCode 2873. Maximum Value of an Ordered Triplet I — Easy
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/
# Submission 2198426689 — Accepted, Python3
#
# My thinking: for the middle element of a triplet I
# want the biggest number before it and the biggest
# number after it — those give the largest possible
# value for that middle spot. I try every middle
# spot and keep the best result, never letting it
# drop below zero.

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0
        for j in range(1, n - 1):
            left_best = max(nums[:j])
            right_best = max(nums[j + 1:])
            best = max(best, (left_best - nums[j]) * right_best)
        return best
