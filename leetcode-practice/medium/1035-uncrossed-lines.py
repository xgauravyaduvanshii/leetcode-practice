# LeetCode 1035. Uncrossed Lines — Medium
# https://leetcode.com/problems/uncrossed-lines/
# Submission 2198990246 — Accepted, Python3
#
# My thinking: this is the longest common
# subsequence of the two arrays. When the numbers
# match, the line adds one to the best before
# them; otherwise I carry forward the best of
# skipping one from either side.

from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
