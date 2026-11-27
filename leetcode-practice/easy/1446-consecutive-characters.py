# LeetCode 1446. Consecutive Characters — Easy
# https://leetcode.com/problems/consecutive-characters/
# Submission 2197579575 — Accepted, Python3
#
# My thinking: I scan the string keeping the length
# of the current run of equal characters. When the
# character changes, the run restarts at 1. The
# longest run I ever see is the answer.

class Solution:
    def maxPower(self, s: str) -> int:
        best = 1
        current = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
                best = max(best, current)
            else:
                current = 1
        return best
