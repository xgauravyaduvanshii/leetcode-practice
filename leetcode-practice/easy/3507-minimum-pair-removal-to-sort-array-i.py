# 3507. Minimum Pair Removal to Sort Array I (Easy)
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/
# Submission 2200025601 — Accepted, Python3
from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # My thinking: the array is sorted when every
        # neighbour goes up or stays level. While it
        # is not, I drop the neighbouring pair whose
        # sum is smallest — the leftmost one if two
        # tie — and count one operation each time.
        nums = nums[:]
        ops = 0
        while nums != sorted(nums):
            best_i = 0
            best_sum = nums[0] + nums[1]
            for i in range(1, len(nums) - 1):
                if nums[i] + nums[i + 1] < best_sum:
                    best_sum = nums[i] + nums[i + 1]
                    best_i = i
            nums = nums[:best_i] + nums[best_i + 2:]
            ops += 1
        return ops
