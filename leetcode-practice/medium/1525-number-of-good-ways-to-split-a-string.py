# LeetCode 1525. Number of Good Ways to Split a String — Medium
# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/
# Submission 2199869356 — Accepted, Python3
#
# My thinking: I sweep the split point from
# left to right, keeping the distinct letters
# on each side. A split is good when both
# sides hold the same number of distinct
# letters.

from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        right = Counter(s)
        left = set()
        good = 0
        for i in range(len(s) - 1):
            left.add(s[i])
            right[s[i]] -= 1
            if right[s[i]] == 0:
                del right[s[i]]
            if len(left) == len(right):
                good += 1
        return good
