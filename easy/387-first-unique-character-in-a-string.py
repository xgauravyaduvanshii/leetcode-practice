# 387. First Unique Character in a String (Easy)
# https://leetcode.com/problems/first-unique-character-in-a-string/
# Submission 2199958139 — Accepted, Python3
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # My thinking: count how often each letter shows
        # up, then walk the string from the front — the
        # first letter whose count is one is the answer.
        counts = Counter(s)
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1
