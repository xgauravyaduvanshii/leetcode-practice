# 3438. Find Valid Pair of Adjacent Digits in String (Easy)
# https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/
# Submission 2200015792 — Accepted, Python3
from collections import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        # My thinking: count how often each digit
        # appears. Then scan the string for the first
        # neighbouring pair of different digits where
        # each digit's total count matches its own
        # value.
        counts = Counter(s)
        for i in range(len(s) - 1):
            a, b = s[i], s[i + 1]
            if a != b and counts[a] == int(a) and counts[b] == int(b):
                return a + b
        return ""
