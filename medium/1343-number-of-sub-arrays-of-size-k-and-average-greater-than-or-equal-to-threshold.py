# LeetCode 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold — Medium
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
# Submission 2199036198 — Accepted, Python3
#
# My thinking: a sliding window holds the sum
# of the current k numbers. A window counts
# when its sum reaches k times the threshold,
# and each step drops one number and takes the
# next.

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = sum(arr[:k])
        count = 1 if window >= k * threshold else 0
        for i in range(k, len(arr)):
            window += arr[i] - arr[i - k]
            if window >= k * threshold:
                count += 1
        return count
