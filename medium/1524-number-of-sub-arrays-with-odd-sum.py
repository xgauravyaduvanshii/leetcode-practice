# LeetCode 1524. Number of Sub-arrays With Odd Sum — Medium
# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
# Submission 2199868963 — Accepted, Python3
#
# My thinking: a subarray sum is odd exactly
# when its two prefix sums have different
# parity. I count how many even and odd
# prefixes I have seen, and each new prefix
# pairs with all of the opposite kind.

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        odd_prefix = 0
        even_prefix = 1
        prefix = 0
        total = 0
        for value in arr:
            prefix += value
            if prefix % 2 == 0:
                total = (total + odd_prefix) % mod
                even_prefix += 1
            else:
                total = (total + even_prefix) % mod
                odd_prefix += 1
        return total
