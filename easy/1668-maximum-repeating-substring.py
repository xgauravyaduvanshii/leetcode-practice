# LeetCode 1668. Maximum Repeating Substring — Easy
# https://leetcode.com/problems/maximum-repeating-substring/
# Submission 2197592656 — Accepted, Python3
#
# My thinking: I try k = 1, 2, 3... and check
# whether the word repeated k times appears in
# the sequence. The largest k that works is the
# answer.

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        while word * (k + 1) in sequence:
            k += 1
        return k
