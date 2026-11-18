# LeetCode 2859. Sum of Values at Indices With K Set Bits — Easy
# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/
# Submission 2198423803 — Accepted, Python3
#
# My thinking: I look at each index, count the 1
# bits in it, and add the value at that index only
# when the count is exactly k. One pass through
# the list is all it takes.

from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(num for i, num in enumerate(nums) if bin(i).count("1") == k)
