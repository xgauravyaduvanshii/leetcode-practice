# LeetCode 908. Smallest Range I — Easy
# https://leetcode.com/problems/smallest-range-i/
# Submission 2197541376 — Accepted, Python3
#
# My thinking: only the smallest and biggest numbers
# matter. I can move the smallest up by k and the
# biggest down by k, so the gap shrinks by 2k — but
# it can never go below zero.

class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2 * k)
