# LeetCode 2729. Check if The Number is Fascinating — Easy
# https://leetcode.com/problems/check-if-the-number-is-fascinating/
# Submission 2197821743 — Accepted, Python3
#
# My thinking: a number is fascinating when n, 2n
# and 3n together use each digit from 1 to 9
# exactly once. I join the three numbers and check
# the sorted digits.

class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n) + str(2 * n) + str(3 * n)
        return sorted(s) == list('123456789')
