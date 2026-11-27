# LeetCode 88. Merge Sorted Array — Easy
# https://leetcode.com/problems/merge-sorted-array/
# Submission 2197384934 — Accepted, Python3
#
# My thinking: nums1 has room at the back, so I merge
# from the end backwards — that way I never overwrite a
# value in nums1 that I still need to compare.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Fill nums1 from the back so we never overwrite a value we still need.
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
