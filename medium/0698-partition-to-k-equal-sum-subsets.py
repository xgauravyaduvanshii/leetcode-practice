# LeetCode 698. Partition to K Equal Sum Subsets — Medium
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# Submission 2198916569 — Accepted, Python3
#
# My thinking: every group must reach the same
# total, so I place the numbers biggest first into
# k groups, skipping a group that would overflow.
# An empty group that fails means no other empty
# group would work either.

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        groups = [0] * k

        def fill(index):
            if index == len(nums):
                return all(group == target for group in groups)
            for i in range(k):
                if groups[i] + nums[index] <= target:
                    groups[i] += nums[index]
                    if fill(index + 1):
                        return True
                    groups[i] -= nums[index]
                if groups[i] == 0:
                    break
            return False

        return fill(0)
