# LeetCode 1422. Maximum Score After Splitting a String — Easy
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/
# Submission 2197578006 — Accepted, Python3
#
# My thinking: the score of a split is the zeros on
# the left plus the ones on the right. I sweep the
# split point from left to right, keeping a running
# count of zeros seen and ones remaining, and track
# the best score I find.

class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count("1")
        zeros = 0
        ones = total_ones
        best = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                zeros += 1
            else:
                ones -= 1
            best = max(best, zeros + ones)
        return best
