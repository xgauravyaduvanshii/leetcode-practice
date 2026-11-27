# LeetCode 2401. Longest Nice Subarray — Medium
# https://leetcode.com/problems/longest-nice-subarray/
# Submission 2204783856 — Accepted, Python3
#
# My thinking: a subarray is nice when no two numbers share a set bit.
# A sliding window tracks the OR of the bits used so far; when the new
# number clashes with a used bit, I drop numbers from the left (XORing
# their bits out) until the clash is gone. The longest window seen is
# the answer.
class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        used = 0
        left = 0
        ans = 0
        for right, x in enumerate(nums):
            while used & x:
                used ^= nums[left]
                left += 1
            used |= x
            if right - left + 1 > ans:
                ans = right - left + 1
        return ans
