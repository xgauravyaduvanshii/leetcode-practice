# LeetCode 1657. Determine if Two Strings Are Close — Medium
# https://leetcode.com/problems/determine-if-two-strings-are-close/
# Submission 2199902169 — Accepted, Python3
#
# My thinking: swapping letters only renames
# them, and swapping whole groups only moves
# counts around. So the two strings must use
# the same letters with the same multiset of
# counts.

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        c1 = Counter(word1)
        c2 = Counter(word2)
        return set(c1) == set(c2) and sorted(c1.values()) == sorted(c2.values())
