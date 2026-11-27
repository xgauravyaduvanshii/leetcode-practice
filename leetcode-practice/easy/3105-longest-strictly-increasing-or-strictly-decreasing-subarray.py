# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray (Easy)
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
# Submission 2199975366 — Accepted, Python3
from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # My thinking: walk along once, keeping the
        # length of the rising run and the falling run
        # ending here. A rise extends the rising run and
        # resets the falling one, a fall does the
        # opposite, and equal neighbours reset both —
        # the best run seen is the answer.
        best = 1
        up = 1
        down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up += 1
                down = 1
            elif nums[i] < nums[i - 1]:
                down += 1
                up = 1
            else:
                up = 1
                down = 1
            best = max(best, up, down)
        return best
