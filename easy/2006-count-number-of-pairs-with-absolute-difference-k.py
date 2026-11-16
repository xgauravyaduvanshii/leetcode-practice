# LeetCode 2006. Count Number of Pairs With Absolute Difference K — Easy
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
# Submission 2197608876 — Accepted, Python3
#
# My thinking: I check every pair of positions once
# and count the pairs whose values differ by exactly
# k.

class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count
