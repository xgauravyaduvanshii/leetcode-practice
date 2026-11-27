# LeetCode 1027. Longest Arithmetic Subsequence — Medium
# https://leetcode.com/problems/longest-arithmetic-subsequence/
# Submission 2198989336 — Accepted, Python3
#
# My thinking: for each pair of positions I keep
# the length of the best arithmetic run ending
# there with their difference. Extending a run
# from an earlier position is just one plus its
# length.

from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [dict() for _ in range(n)]
        best = 2
        for j in range(n):
            for i in range(j):
                diff = nums[j] - nums[i]
                length = dp[i].get(diff, 1) + 1
                dp[j][diff] = length
                best = max(best, length)
        return best
