# 3375. Minimum Operations to Make Array Values Equal to K (Easy)
# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/
# Submission 2200008772 — Accepted, Python3
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # My thinking: an operation picks one value and
        # drops every copy of it down to a smaller one,
        # so each distinct value above k needs exactly
        # one operation. But if any value is already
        # below k, it can never be raised — impossible.
        if any(v < k for v in nums):
            return -1
        return len({v for v in nums if v > k})
