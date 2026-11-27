# LeetCode 2430. Maximum Deletions on a String — Hard
# https://leetcode.com/problems/maximum-deletions-on-a-string/
# Submission 2201736226 — Accepted, Python3
#
# My thinking: deleting more means cutting
# smaller matching pieces — I first learn
# how long any two suffixes agree, then
# from each position I take the best cut
# whose two halves match, or just sweep
# the rest away in one go.

class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            best = 0
            max_j = (n - i) // 2
            for j in range(1, max_j + 1):
                if lcp[i][i + j] >= j:
                    best = max(best, dp[i + j])
            dp[i] = best + 1
        return dp[0]
