# LeetCode 2546. Apply Bitwise Operations to Make Strings Equal — Medium
# https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/
# Submission 2205059311 — Accepted, Python3
#
# My thinking: the operations can turn any 1 into any pattern
# elsewhere, but they can never create a 1 out of all zeros. So
# equal strings are fine, and otherwise both strings need at
# least one 1.
class Solution:
    def makeStringsEqual(self, s: str, t: str) -> bool:
        if s == t:
            return True
        return "1" in s and "1" in t
