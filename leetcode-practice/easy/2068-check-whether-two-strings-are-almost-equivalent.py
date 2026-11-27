# LeetCode 2068. Check Whether Two Strings are Almost Equivalent — Easy
# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/
# Submission 2197611590 — Accepted, Python3
#
# My thinking: I count the letters in both words and
# compare the counts letter by letter. The words are
# almost equivalent when no letter's counts differ
# by more than 3.

from collections import Counter


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if abs(c1[ch] - c2[ch]) > 3:
                return False
        return True
