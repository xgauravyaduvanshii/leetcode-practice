# LeetCode 2255. Count Prefixes of a Given String — Easy
# https://leetcode.com/problems/count-prefixes-of-a-given-string/
# Submission 2197620345 — Accepted, Python3
#
# My thinking: I count the words that are a prefix
# of the given string — that is, the string starts
# with that word.

class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        return sum(1 for w in words if s.startswith(w))
