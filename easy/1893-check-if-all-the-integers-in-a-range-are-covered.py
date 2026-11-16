# LeetCode 1893. Check if All the Integers in a Range Are Covered — Easy
# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
# Submission 2197603200 — Accepted, Python3
#
# My thinking: I collect every integer covered by
# any of the given ranges into a set, then check
# that each number from left to right is in it.

class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        covered = set()
        for a, b in ranges:
            for x in range(a, b + 1):
                covered.add(x)
        return all(x in covered for x in range(left, right + 1))
