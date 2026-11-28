# LeetCode 2425. Bitwise XOR of All Pairings — Medium
# https://leetcode.com/problems/bitwise-xor-of-all-pairings/
# Submission 2204862104 — Accepted, Python3
#
# My thinking: every nums1 value appears len(nums2) times among the
# pairings and every nums2 value appears len(nums1) times. A value
# appearing an even number of times XORs away to zero, so only the XOR
# of nums1 (when len(nums2) is odd) and the XOR of nums2 (when
# len(nums1) is odd) survive.
from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if len(nums2) % 2 == 1:
            for x in nums1:
                ans ^= x
        if len(nums1) % 2 == 1:
            for x in nums2:
                ans ^= x
        return ans
