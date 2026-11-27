# 338. Counting Bits (Easy)
# https://leetcode.com/problems/counting-bits/
# Submission 2199957889 — Accepted, Python3
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # My thinking: dropping the last bit of a number
        # halves it, so its bit count is the halved
        # number's count plus one if the dropped bit was
        # a 1. Building the answers in order reuses each
        # earlier answer once.
        bits = [0] * (n + 1)
        for i in range(1, n + 1):
            bits[i] = bits[i >> 1] + (i & 1)
        return bits
