# LeetCode 740. Delete and Earn — Medium
# https://leetcode.com/problems/delete-and-earn/
# Submission 2198925074 — Accepted, Python3
#
# My thinking: taking a number earns all its
# copies but forbids its neighbours, which is the
# same as the house-robber choice on the points
# each value is worth. I keep only the take and
# skip totals as I go.

from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = [0] * (max(nums) + 1)
        for num in nums:
            points[num] += num
        take, skip = 0, 0
        for value in points:
            take, skip = max(take, skip + value), take
        return max(take, skip)
