# LeetCode 1663. Smallest String With A Given Numeric Value — Medium
# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
# Submission 2199905834 — Accepted, Python3
#
# My thinking: I want the smallest string, so
# I push the value to the rightmost letters.
# Each spot takes as much as it can, up to z,
# and the rest stays to its left.

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        chars = ["a"] * n
        k -= n
        i = n - 1
        while k > 0:
            add = min(25, k)
            chars[i] = chr(ord("a") + add)
            k -= add
            i -= 1
        return "".join(chars)
