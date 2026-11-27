# 3550. Smallest Index With Digit Sum Equal to Index (Easy)
# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
# Submission 2200027569 — Accepted, Python3
from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        # My thinking: walk the array from the start
        # and return the first spot where the digit
        # sum of the number equals its own position.
        for i, num in enumerate(nums):
            if sum(int(d) for d in str(num)) == i:
                return i
        return -1
