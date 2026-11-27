# 4092. Binary Digit Score (Easy)
# https://leetcode.com/problems/binary-digit-score/
# Submission 2200104577 — Accepted, Python3
class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        # My thinking: I count the set bits in each
        # number. When the first count is at least the
        # second, the score is their product —
        # otherwise it is the second divided by the
        # first.
        s1 = bin(a).count("1")
        s2 = bin(b).count("1")
        return s1 * s2 if s1 >= s2 else s2 // s1
