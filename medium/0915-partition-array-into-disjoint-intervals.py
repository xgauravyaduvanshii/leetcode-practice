# LeetCode 915. Partition Array into Disjoint Intervals — Medium
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/
# Submission 2198968861 — Accepted, Python3
#
# My thinking: the split works when the biggest
# value on the left is no bigger than the
# smallest on the right. I precompute both sides
# and take the first split where that holds.

from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        left_max = [0] * n
        right_min = [0] * n
        running = nums[0]
        for i in range(n):
            running = max(running, nums[i])
            left_max[i] = running
        running = nums[-1]
        for i in range(n - 1, -1, -1):
            running = min(running, nums[i])
            right_min[i] = running
        for i in range(n - 1):
            if left_max[i] <= right_min[i + 1]:
                return i + 1
        return n - 1
