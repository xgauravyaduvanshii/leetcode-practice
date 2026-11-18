# LeetCode 718. Maximum Length of Repeated Subarray — Medium
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# Submission 2198918633 — Accepted, Python3
#
# My thinking: when two numbers match, the common
# stretch ending there is one longer than the
# stretch ending just before them. I build those
# lengths up with two rows of DP and keep the
# biggest one.

from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        prev = [0] * (len(nums2) + 1)
        best = 0
        for i in range(1, len(nums1) + 1):
            current = [0] * (len(nums2) + 1)
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    current[j] = prev[j - 1] + 1
                    best = max(best, current[j])
            prev = current
        return best
