# 1009. Complement of Base 10 Integer (Easy)
# https://leetcode.com/problems/complement-of-base-10-integer/
# Submission 2199965779 — Accepted, Python3
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # My thinking: the complement only flips the bits
        # the number actually uses, so I build a mask of
        # all ones as long as the number, then flip the
        # number against that mask. Zero is special — its
        # complement is 1.
        if n == 0:
            return 1
        mask = 1
        while mask <= n:
            mask <<= 1
        return (mask - 1) ^ n
