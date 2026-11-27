# LeetCode 2475. Number of Unequal Triplets in Array — Easy
# https://leetcode.com/problems/number-of-unequal-triplets-in-array/
# Submission 2197790403 — Accepted, Python3
#
# My thinking: I check every triplet of positions
# and count the ones where all three values are
# different from each other.

class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                        count += 1
        return count
