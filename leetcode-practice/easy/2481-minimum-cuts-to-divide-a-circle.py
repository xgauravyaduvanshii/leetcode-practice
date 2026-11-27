# LeetCode 2481. Minimum Cuts to Divide a Circle — Easy
# https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/
# Submission 2197790906 — Accepted, Python3
#
# My thinking: one slice needs no cuts. For an even
# number of slices, each cut through the centre
# makes two slices, so n/2 cuts. For an odd number
# of slices, one cut can't pass through the centre
# and make two slices, so it takes n cuts.

class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        return n // 2 if n % 2 == 0 else n
