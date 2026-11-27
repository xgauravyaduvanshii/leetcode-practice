# LeetCode 2370. Longest Ideal Subsequence — Medium
# https://leetcode.com/problems/longest-ideal-subsequence/
# Submission 2204757735 — Accepted, Python3
#
# My thinking: dp[c] is the longest ideal subsequence ending with letter
# c. For each new letter I look at all letters within k of it and extend
# the best of those subsequences by one. Only 26 letters exist, so a
# scan of the window is cheap, and the answer is the largest dp value.
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for ch in s:
            c = ord(ch) - ord('a')
            lo = max(0, c - k)
            hi = min(25, c + k)
            best = 0
            for j in range(lo, hi + 1):
                if dp[j] > best:
                    best = dp[j]
            dp[c] = best + 1
        return max(dp)
