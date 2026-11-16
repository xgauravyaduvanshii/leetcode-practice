# LeetCode 1356. Sort Integers by The Number of 1 Bits — Easy
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
# Submission 2197572495 — Accepted, Python3
#
# My thinking: I sort by two things — first by how
# many 1 bits the number has in binary, then by
# the number itself when the bit counts tie. Python
# sorts tuples exactly that way.

class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))
