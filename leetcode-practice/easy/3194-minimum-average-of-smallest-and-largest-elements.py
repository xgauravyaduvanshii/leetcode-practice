# 3194. Minimum Average of Smallest and Largest Elements (Easy)
# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/
# Submission 2199984679 — Accepted, Python3
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        # My thinking: sort the numbers, then pair the
        # smallest with the largest, the next smallest
        # with the next largest, and so on. The smallest
        # average among those pairs is the answer.
        nums.sort()
        best = float("inf")
        n = len(nums)
        for i in range(n // 2):
            best = min(best, (nums[i] + nums[n - 1 - i]) / 2)
        return best
