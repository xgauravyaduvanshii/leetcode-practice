# 3954. Sum of Compatible Numbers in Range I (Easy)
# https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/
# Submission 2200091355 — Accepted, Python3
class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        # My thinking: I check every positive number
        # within k of n, and keep the ones that share
        # no set bit with n at all.
        return sum(x for x in range(max(1, n - k), n + k + 1) if (n & x) == 0)
