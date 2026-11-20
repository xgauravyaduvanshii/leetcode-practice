# LeetCode 1498. Number of Subsequences That Satisfy the Given Sum Condition — Medium
# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
# Submission 2199864569 — Accepted, Python3
#
# My thinking: after sorting, a subsequence's
# smallest and largest elements decide it. For
# each smallest element I find the farthest
# largest that still fits, and every choice in
# between doubles the count.

from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10 ** 9 + 7
        powers = [1] * len(nums)
        for i in range(1, len(nums)):
            powers[i] = powers[i - 1] * 2 % mod
        total = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                total = (total + powers[right - left]) % mod
                left += 1
            else:
                right -= 1
        return total
