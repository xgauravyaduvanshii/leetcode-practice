# LeetCode 2600. K Items With the Maximum Sum — Easy
# https://leetcode.com/problems/k-items-with-the-maximum-sum/
# Submission 2197808679 — Accepted, Python3
#
# My thinking: to maximise the sum I take 1s first,
# then 0s, then -1s — whatever of k is left after
# the 1s and 0s must be -1s, and each one subtracts
# 1 from the total.

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        take_ones = min(k, numOnes)
        k -= take_ones
        take_zeros = min(k, numZeros)
        k -= take_zeros
        return take_ones - k
