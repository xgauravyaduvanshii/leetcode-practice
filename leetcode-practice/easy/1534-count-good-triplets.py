# LeetCode 1534. Count Good Triplets — Easy
# https://leetcode.com/problems/count-good-triplets/
# Submission 2197584722 — Accepted, Python3
#
# My thinking: I try every triplet i < j < k and
# check the three conditions on their differences.
# The array is small enough that a triple loop is
# fine — I skip early when the first pair already
# fails.

from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, n):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count
