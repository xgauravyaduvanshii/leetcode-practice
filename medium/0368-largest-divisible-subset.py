# LeetCode 368. Largest Divisible Subset — Medium
# https://leetcode.com/problems/largest-divisible-subset/
# Submission 2198758162 — Accepted, Python3
#
# My thinking: after sorting, a number can only
# follow a smaller number that divides it. I build
# the longest chain ending at each number, remember
# where each chain came from, and walk back from the
# longest one.

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        previous = [-1] * n
        best_index = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    previous[i] = j
            if dp[i] > dp[best_index]:
                best_index = i
        subset = []
        index = best_index
        while index != -1:
            subset.append(nums[index])
            index = previous[index]
        return subset[::-1]
