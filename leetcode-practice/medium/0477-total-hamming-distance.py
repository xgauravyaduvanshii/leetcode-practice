# LeetCode 477. Total Hamming Distance — Medium
# https://leetcode.com/problems/total-hamming-distance/
# Submission 2198820039 — Accepted, Python3
#
# My thinking: each bit position is independent — a
# pair differs there exactly when one number has a
# 1 and the other a 0. So I count the ones at each
# position and multiply by the zeros.

from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        for bit in range(32):
            ones = sum((num >> bit) & 1 for num in nums)
            total += ones * (len(nums) - ones)
        return total
