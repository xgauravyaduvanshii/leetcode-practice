# 4074. Maximum Product Pair With Target Sum (Easy)
# https://leetcode.com/problems/maximum-product-pair-with-target-sum/
# Submission 2200102969 — Accepted, Python3
class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        # My thinking: I try every pair of indices,
        # keep the ones that add up to the target with
        # the first value bigger, and remember the
        # pair whose product is largest.
        best = None
        best_prod = None
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if nums[i] + nums[j] == target and nums[i] > nums[j]:
                    prod = nums[i] * nums[j]
                    if best_prod is None or prod > best_prod:
                        best_prod = prod
                        best = [i, j]
        return best if best is not None else [-1, -1]
