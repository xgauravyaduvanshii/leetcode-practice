# LeetCode 1143. Longest Common Subsequence — Medium
# https://leetcode.com/problems/longest-common-subsequence/
# Submission 2199004851 — Accepted, Python3
#
# My thinking: I build a table row by row — when
# two letters match, the answer grows by one
# over the diagonal; when they differ, I carry
# the best of the row above or the cell beside.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        previous = [0] * (len(text2) + 1)
        for a in text1:
            current = [0] * (len(text2) + 1)
            for j, b in enumerate(text2, 1):
                if a == b:
                    current[j] = previous[j - 1] + 1
                else:
                    current[j] = max(previous[j], current[j - 1])
            previous = current
        return previous[-1]
