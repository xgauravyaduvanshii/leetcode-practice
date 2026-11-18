# LeetCode 583. Delete Operation for Two Strings — Medium
# https://leetcode.com/problems/delete-operation-for-two-strings/
# Submission 2198875214 — Accepted, Python3
#
# My thinking: every letter the two words share
# can stay, so the deletions are just the letters
# outside their longest common subsequence. I
# compute that subsequence with two rows of DP.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prev = [0] * (n + 1)
        for i in range(1, m + 1):
            current = [0] * (n + 1)
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    current[j] = prev[j - 1] + 1
                else:
                    current[j] = max(prev[j], current[j - 1])
            prev = current
        return m + n - 2 * prev[n]
