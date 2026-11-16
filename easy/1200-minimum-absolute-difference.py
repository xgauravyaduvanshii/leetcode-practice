# LeetCode 1200. Minimum Absolute Difference — Easy
# https://leetcode.com/problems/minimum-absolute-difference/
# Submission 2197562751 — Accepted, Python3
#
# My thinking: after sorting, the closest pair must
# be neighbours — so I only need to check adjacent
# pairs. I find the smallest gap first, then
# collect every neighbouring pair that has exactly
# that gap.

class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        min_diff = min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))
        return [[arr[i], arr[i + 1]] for i in range(len(arr) - 1) if arr[i + 1] - arr[i] == min_diff]
