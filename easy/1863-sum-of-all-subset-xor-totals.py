# LeetCode 1863. Sum of All Subset XOR Totals — Easy
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/
# Submission 2197601962 — Accepted, Python3
#
# My thinking: I enumerate every subset with a
# bitmask — each bit says whether that element is
# in the subset. For each subset I xor its elements
# together and add the result to the total.

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        total = 0
        n = len(nums)
        for mask in range(1 << n):
            x = 0
            for i in range(n):
                if mask >> i & 1:
                    x ^= nums[i]
            total += x
        return total
