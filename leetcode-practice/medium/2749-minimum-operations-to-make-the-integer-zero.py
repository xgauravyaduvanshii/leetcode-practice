# LeetCode 2749. Minimum Operations to Make the Integer Zero — Medium
# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/
# Submission 2198359166 — Accepted, Python3
#
# My thinking: after k operations the number left
# is num1 - k * num2, and it must be a sum of
# exactly k powers of two. That works only when
# the leftover is at least k (one per power) and
# its binary form has at most k ones — I can split
# a power of two into smaller ones to reach k
# terms. I try k from 1 upwards and take the
# first one that fits.

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            left = num1 - k * num2
            if left >= k and bin(left).count("1") <= k:
                return k
        return -1
