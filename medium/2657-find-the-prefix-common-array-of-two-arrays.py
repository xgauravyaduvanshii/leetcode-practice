# LeetCode 2657. Find the Prefix Common Array of Two Arrays — Medium
# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
# Submission 2197813354 — Accepted, Python3
#
# My thinking: I scan both arrays together, keeping
# the values seen so far in each. A value becomes
# common when it appears in the other array's seen
# set, or when both arrays show the same value at
# the same position.

from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen_a = set()
        seen_b = set()
        res = []
        common = 0
        for a, b in zip(A, B):
            if a in seen_b:
                common += 1
            if b in seen_a:
                common += 1
            if a == b:
                common += 1
            seen_a.add(a)
            seen_b.add(b)
            res.append(common)
        return res
