# 3364. Minimum Positive Sum Subarray (Easy)
# https://leetcode.com/problems/minimum-positive-sum-subarray/
# Submission 2200008114 — Accepted, Python3
from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # My thinking: check every subarray whose length
        # sits between l and r, and keep the smallest
        # sum that is still positive. If no subarray
        # manages a positive sum, the answer is -1.
        best = None
        for start in range(len(nums)):
            total = 0
            for end in range(start, min(len(nums), start + r)):
                total += nums[end]
                if end - start + 1 >= l and total > 0:
                    if best is None or total < best:
                        best = total
        return -1 if best is None else best
