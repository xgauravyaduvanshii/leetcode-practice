# LeetCode 1053. Previous Permutation With One Swap — Medium
# https://leetcode.com/problems/previous-permutation-with-one-swap/
# Submission 2198993787 — Accepted, Python3
#
# My thinking: I find the rightmost spot where
# the array still goes down, then swap it with
# the biggest smaller value to its right — the
# leftmost copy when there are duplicates, so
# the tail stays as big as possible.

from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                break
        else:
            return arr
        best = -1
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                if best == -1 or arr[j] > arr[best]:
                    best = j
        arr[i], arr[best] = arr[best], arr[i]
        return arr
