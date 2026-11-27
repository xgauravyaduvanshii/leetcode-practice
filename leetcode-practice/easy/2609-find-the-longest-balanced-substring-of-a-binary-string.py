# LeetCode 2609. Find the Longest Balanced Substring of a Binary String — Easy
# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/
# Submission 2197810547 — Accepted, Python3
#
# My thinking: a balanced substring is a run of 0s
# followed by the same number of 1s. I walk through
# the string counting each run of 0s and the 1s
# after it, and the best length is twice the smaller
# of the two counts.

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        best = 0
        i = 0
        n = len(s)
        while i < n:
            zeros = 0
            while i < n and s[i] == '0':
                zeros += 1
                i += 1
            ones = 0
            while i < n and s[i] == '1':
                ones += 1
                i += 1
            best = max(best, 2 * min(zeros, ones))
        return best
