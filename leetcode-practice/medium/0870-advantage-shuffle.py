# LeetCode 870. Advantage Shuffle — Medium
# https://leetcode.com/problems/advantage-shuffle/
# Submission 2198960314 — Accepted, Python3
#
# My thinking: I play the biggest targets first.
# When the biggest card I have left beats one, I
# use it; when nothing beats it, I sacrifice my
# smallest card instead.

from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        result = [0] * len(nums2)
        order = sorted(range(len(nums2)), key=lambda i: nums2[i])
        left, right = 0, len(nums1) - 1
        for i in reversed(order):
            if nums1[right] > nums2[i]:
                result[i] = nums1[right]
                right -= 1
            else:
                result[i] = nums1[left]
                left += 1
        return result
