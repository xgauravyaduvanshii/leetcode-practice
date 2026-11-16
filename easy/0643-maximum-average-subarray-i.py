# LeetCode 643. Maximum Average Subarray I — Easy
# https://leetcode.com/problems/maximum-average-subarray-i/
# Submission 2197508829 — Accepted, Python3
#
# My thinking: a sliding window of size k. I add up
# the first window, then slide it one step at a
# time — add the new number coming in, subtract
# the one going out. I keep the biggest window sum
# I see, and divide by k at the end.

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window = sum(nums[:k])
        best = window
        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]
            best = max(best, window)
        return best / k
