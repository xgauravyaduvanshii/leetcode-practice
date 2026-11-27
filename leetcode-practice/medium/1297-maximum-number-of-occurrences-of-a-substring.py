# LeetCode 1297. Maximum Number of Occurrences of a Substring — Medium
# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/
# Submission 2199026858 — Accepted, Python3
#
# My thinking: only the shortest allowed
# substrings matter — any longer one contains a
# shorter one that appears at least as often.
# I count every window of that size with few
# enough distinct letters.

from collections import Counter


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = Counter()
        for i in range(len(s) - minSize + 1):
            piece = s[i:i + minSize]
            if len(set(piece)) <= maxLetters:
                counts[piece] += 1
        return max(counts.values(), default=0)
