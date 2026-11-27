# LeetCode 2185. Counting Words With a Given Prefix — Easy
# https://leetcode.com/problems/counting-words-with-a-given-prefix/
# Submission 2197616791 — Accepted, Python3
#
# My thinking: I just count the words that start with
# the given prefix.

class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        return sum(1 for w in words if w.startswith(pref))
