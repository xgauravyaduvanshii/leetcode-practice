# LeetCode 1540. Can Convert String in K Moves — Medium
# https://leetcode.com/problems/can-convert-string-in-k-moves/
# Submission 2199871523 — Accepted, Python3
#
# My thinking: each position needs one shift,
# and the same shift size can only be used on
# moves shift, shift + 26, shift + 52, and so
# on. The busiest shift decides whether k
# moves are enough.

from collections import Counter


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        needs = Counter()
        for a, b in zip(s, t):
            shift = (ord(b) - ord(a)) % 26
            if shift:
                needs[shift] += 1
        for shift, count in needs.items():
            if shift + (count - 1) * 26 > k:
                return False
        return True
