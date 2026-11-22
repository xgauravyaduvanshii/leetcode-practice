# LeetCode 1755. Closest Subsequence Sum — Hard
# https://leetcode.com/problems/closest-subsequence-sum/
# Submission 2201144194 — Accepted, Python3
#
# My thinking: I split the numbers in half, list
# every subset sum of each half, sort one half, and
# for each sum in the other half I binary-search the
# closest partner to the goal.

from bisect import bisect_left

class Solution:
    def minAbsDifference(self, nums: list[int], goal: int) -> int:
        def subset_sums(arr):
            sums = [0]
            for v in arr:
                sums += [s + v for s in sums]
            return sums
        n = len(nums)
        left = subset_sums(nums[:n // 2])
        right = subset_sums(nums[n // 2:])
        right.sort()
        best = abs(goal)
        for s in left:
            target = goal - s
            i = bisect_left(right, target)
            for j in (i - 1, i):
                if 0 <= j < len(right):
                    best = min(best, abs(s + right[j] - goal))
        return best
