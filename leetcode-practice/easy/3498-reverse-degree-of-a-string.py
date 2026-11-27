# 3498. Reverse Degree of a String (Easy)
# https://leetcode.com/problems/reverse-degree-of-a-string/
# Submission 2200022022 — Accepted, Python3
class Solution:
    def reverseDegree(self, s: str) -> int:
        # My thinking: each letter's reverse degree is
        # its distance from the end of the alphabet —
        # a counts 26, z counts 1. I multiply each by
        # its position in the string and add them up.
        return sum((26 - (ord(ch) - ord("a"))) * (i + 1) for i, ch in enumerate(s))
