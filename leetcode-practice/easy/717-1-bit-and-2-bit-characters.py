# 717. 1-bit and 2-bit Characters (Easy)
# https://leetcode.com/problems/1-bit-and-2-bit-characters/
# Submission 2199963781 — Accepted, Python3
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # My thinking: read the bits from the front. A 1
        # always starts a two-bit character, a 0 is a
        # one-bit character on its own. If the walk lands
        # exactly on the last bit, that bit is a one-bit
        # character; if it jumps over it, it is not.
        i = 0
        n = len(bits)
        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == n - 1
