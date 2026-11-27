# LeetCode 1005. Maximize Sum Of Array After K Negations — Easy
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
# Submission 2197550449 — Accepted, Python3
#
# My thinking: flipping a negative number to positive
# always helps, so I sort the array and flip the
# negatives first, smallest first. If I still have
# flips left, flipping the same number twice
# cancels out — so only an odd leftover matters,
# and then I flip the smallest number in the array.

class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort()
        i = 0
        while i < len(nums) and k > 0 and nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1
        if k % 2 == 1:
            nums.sort()
            nums[0] = -nums[0]
        return sum(nums)
