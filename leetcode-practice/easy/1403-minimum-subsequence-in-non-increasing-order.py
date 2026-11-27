# LeetCode 1403. Minimum Subsequence in Non-Increasing Order — Easy
# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/
# Submission 2197576335 — Accepted, Python3
#
# My thinking: taking the biggest numbers first is
# the fastest way to beat the sum of the rest, so I
# sort descending and keep grabbing numbers until
# my pile is strictly bigger than what is left.

class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        sub = []
        sub_sum = 0
        for num in nums:
            sub.append(num)
            sub_sum += num
            if sub_sum > total - sub_sum:
                break
        return sub
