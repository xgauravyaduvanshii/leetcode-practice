# 3090. Maximum Length Substring With Two Occurrences (Easy)
# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/
# Submission 2199974561 — Accepted, Python3
from collections import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # My thinking: slide a window across the string
        # and keep counts inside it. Whenever some
        # letter shows up a third time, shrink the window
        # from the left until every letter is back to at
        # most two — the widest window seen is the answer.
        counts = Counter()
        best = 0
        left = 0
        for right, ch in enumerate(s):
            counts[ch] += 1
            while counts[ch] > 2:
                counts[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
