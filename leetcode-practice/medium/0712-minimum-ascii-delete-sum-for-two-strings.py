# LeetCode 712. Minimum ASCII Delete Sum for Two Strings — Medium
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
# Submission 2198917290 — Accepted, Python3
#
# My thinking: matching letters cost nothing to
# keep, so the cheapest deletions are the ones
# outside the best common subsequence — weighted
# by each letter's ASCII value. Two rows of DP are
# enough.

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        prev = [sum(map(ord, s2[:j])) for j in range(n + 1)]
        for i in range(1, m + 1):
            current = [sum(map(ord, s1[:i]))] + [0] * n
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    current[j] = prev[j - 1]
                else:
                    current[j] = min(prev[j] + ord(s1[i - 1]), current[j - 1] + ord(s2[j - 1]))
            prev = current
        return prev[n]
