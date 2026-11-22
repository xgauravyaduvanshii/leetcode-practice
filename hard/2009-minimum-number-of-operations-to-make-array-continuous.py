# LeetCode 2009. Minimum Number of Operations to Make Array Continuous — Hard
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/
# Submission 2201312011 — Accepted, Python3
#
# My thinking: I only keep the distinct values
# that already fit inside one window of length n,
# and the biggest such window tells me how few
# changes I need.

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        uniq = sorted(set(nums))
        best = 0
        right = 0
        for left in range(len(uniq)):
            while right < len(uniq) and uniq[right] - uniq[left] < n:
                right += 1
            best = max(best, right - left)
        return n - best
