# LeetCode 1186. Maximum Subarray Sum with One Deletion — Medium
# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
# Submission 2199009550 — Accepted, Python3
#
# My thinking: I walk the array keeping two
# running sums — the best ending here with
# nothing deleted, and the best ending here
# with one deletion used. Each step extends or
# restarts either one.

from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        keep = arr[0]
        deleted = 0
        best = arr[0]
        for value in arr[1:]:
            deleted = max(keep, deleted + value)
            keep = max(keep + value, value)
            best = max(best, keep, deleted)
        return best
