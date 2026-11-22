# LeetCode 2223. Sum of Scores of Built Strings — Hard
# https://leetcode.com/problems/sum-of-scores-of-built-strings/
# Submission 2200891654 — Accepted, Python3
#
# My thinking: the score of each suffix is how long it
# matches the whole string from the start, and the
# Z-function computes exactly those match lengths in one
# pass — add them all up.

class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        z = [0] * n
        left = right = 0
        for i in range(1, n):
            if i <= right:
                z[i] = min(right - i + 1, z[i - left])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > right:
                left, right = i, i + z[i] - 1
        return n + sum(z)
