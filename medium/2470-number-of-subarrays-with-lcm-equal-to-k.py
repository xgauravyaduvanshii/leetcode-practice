# LeetCode 2470. Number of Subarrays With LCM Equal to K — Medium
# https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/
# Submission 2204964263 — Accepted, Python3
#
# My thinking: for each start, extend right while accumulating the
# LCM. The LCM only grows, so once it passes k no longer subarray
# from this start can work — stop there. Count the positions where
# the running LCM is exactly k.
import math


class Solution:
    def subarrayLCM(self, nums: list[int], k: int) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            cur = 1
            for j in range(i, n):
                cur = math.lcm(cur, nums[j])
                if cur > k:
                    break
                if cur == k:
                    res += 1
        return res
