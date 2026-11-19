# LeetCode 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit — Medium
# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
# Submission 2199057595 — Accepted, Python3
#
# My thinking: two monotone queues track the
# window's smallest and largest values. When
# they drift too far apart I shrink the window
# from the left until it fits again.

from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mins = deque()
        maxs = deque()
        left = 0
        best = 0
        for right, value in enumerate(nums):
            while mins and nums[mins[-1]] > value:
                mins.pop()
            while maxs and nums[maxs[-1]] < value:
                maxs.pop()
            mins.append(right)
            maxs.append(right)
            while nums[maxs[0]] - nums[mins[0]] > limit:
                if mins[0] == left:
                    mins.popleft()
                if maxs[0] == left:
                    maxs.popleft()
                left += 1
            best = max(best, right - left + 1)
        return best
