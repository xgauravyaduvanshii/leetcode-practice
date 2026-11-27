# LeetCode 4. Median of Two Sorted Arrays — Hard
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Submission 2198361819 — Accepted, Python3
#
# My thinking: I cut both arrays so that everything
# on the left of the cuts is smaller than everything
# on the right, and the left side holds exactly half
# the numbers. I binary search the cut in the shorter
# array — when the biggest left number is no bigger
# than the smallest right number, the median sits
# right at that cut.

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left_count = (m + n + 1) // 2
        lo, hi = 0, m
        while lo <= hi:
            cut1 = (lo + hi) // 2
            cut2 = left_count - cut1
            left1 = nums1[cut1 - 1] if cut1 > 0 else float("-inf")
            right1 = nums1[cut1] if cut1 < m else float("inf")
            left2 = nums2[cut2 - 1] if cut2 > 0 else float("-inf")
            right2 = nums2[cut2] if cut2 < n else float("inf")
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                hi = cut1 - 1
            else:
                lo = cut1 + 1
