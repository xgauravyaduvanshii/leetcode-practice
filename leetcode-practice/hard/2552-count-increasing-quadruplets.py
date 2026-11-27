# LeetCode 2552. Count Increasing Quadruplets — Hard
# https://leetcode.com/problems/count-increasing-quadruplets/
# Submission 2201820376 — Accepted, Python3
#
# My thinking: I fix the middle pair
# and count what can go on either side
# of it — how many smaller numbers sit
# before the left one, and how many
# bigger numbers sit after the right
# one — then multiply and add them up.

import itertools


class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        # freq counts the values seen before j; its prefix sums give, for any
        # k, how many of those are smaller than nums[k].
        freq = [0] * (n + 2)
        for j in range(n):
            pref = list(itertools.accumulate(freq))
            suf = 0
            for k in range(n - 1, j, -1):
                if nums[k] < nums[j]:
                    ans += pref[nums[k] - 1] * suf
                if nums[k] > nums[j]:
                    suf += 1
            freq[nums[j]] += 1
        return ans
