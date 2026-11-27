# LeetCode 1846. Maximum Element After Decreasing and Rearranging — Medium
# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
# Submission 2199946721 — Accepted, Python3
#
# My thinking: after sorting, the first
# element must become one, and each next
# element can be at most one more than the
# one before it. I clamp every element to
# that limit and the last one is the answer.

from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1
        return arr[-1]
