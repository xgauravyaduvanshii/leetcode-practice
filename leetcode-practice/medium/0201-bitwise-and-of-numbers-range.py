# LeetCode 201. Bitwise AND of Numbers Range — Medium
# https://leetcode.com/problems/bitwise-and-of-numbers-range/
# Submission 2198446342 — Accepted, Python3
#
# My thinking: the answer keeps only the bits that
# are the same across the whole range, which are
# exactly the shared leading bits of the two ends.
# I shift both ends right together until they match
# — that is the shared prefix — and shift it back
# by the same amount.

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shifts = 0
        while left != right:
            left >>= 1
            right >>= 1
            shifts += 1
        return left << shifts
