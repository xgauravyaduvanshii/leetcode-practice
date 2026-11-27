# 3750. Minimum Number of Flips to Reverse Binary String (Easy)
# https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/
# Submission 2200061021 — Accepted, Python3
class Solution:
    def minimumFlips(self, n: int) -> int:
        # My thinking: write the number in binary and
        # write that backwards. Every spot where the
        # two differ needs exactly one flip.
        s = bin(n)[2:]
        return sum(1 for a, b in zip(s, s[::-1]) if a != b)
