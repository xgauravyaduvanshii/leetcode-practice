# LeetCode 2465. Number of Distinct Averages — Easy
# https://leetcode.com/problems/number-of-distinct-averages/
# Submission 2197789338 — Accepted, Python3
#
# My thinking: after sorting, I pair the smallest
# remaining number with the largest. The average of
# a pair is decided by its sum, so I count how many
# different pair sums appear.

class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()
        seen = set()
        n = len(nums)
        for i in range(n // 2):
            seen.add(nums[i] + nums[n - 1 - i])
        return len(seen)
