# LeetCode 1947. Maximum Compatibility Score Sum — Medium
# https://leetcode.com/problems/maximum-compatibility-score-sum/
# Submission 2201819694 — Accepted, Python3
#
# My thinking: with at most eight
# students I try every pairing by
# remembering which mentors are already
# taken — each new student picks the
# best free mentor, and the best total
# bubbles up.

class Solution:
    def maxCompatibilitySum(self, students: list[list[int]], mentors: list[list[int]]) -> int:
        m = len(students)
        score = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                score[i][j] = sum(a == b for a, b in zip(students[i], mentors[j]))
        dp = [-1] * (1 << m)
        dp[0] = 0
        for mask in range(1 << m):
            s = bin(mask).count("1")
            if s >= m:
                continue
            for j in range(m):
                if not (mask >> j) & 1:
                    nmask = mask | (1 << j)
                    dp[nmask] = max(dp[nmask], dp[mask] + score[s][j])
        return dp[(1 << m) - 1]
