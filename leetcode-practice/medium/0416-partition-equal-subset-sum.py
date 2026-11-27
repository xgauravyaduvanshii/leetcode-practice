# LeetCode 416. Partition Equal Subset Sum — Medium
# https://leetcode.com/problems/partition-equal-subset-sum/
# Submission 2198784047 — Accepted, Python3
#
# My thinking: a split into two equal halves exists
# exactly when some subset adds up to half the total.
# I grow the set of reachable sums number by number
# and check whether half the total is among them.

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        reachable = {0}
        for num in nums:
            reachable |= {s + num for s in reachable if s + num <= target}
        return target in reachable
