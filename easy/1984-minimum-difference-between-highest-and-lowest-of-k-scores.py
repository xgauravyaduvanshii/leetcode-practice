# LeetCode 1984. Minimum Difference Between Highest and Lowest of K Scores — Easy
# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
# Submission 2197607457 — Accepted, Python3
#
# My thinking: after sorting, the k scores with the
# smallest range must sit next to each other. I
# slide a window of k over the sorted array and take
# the smallest difference between its ends.

class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))
