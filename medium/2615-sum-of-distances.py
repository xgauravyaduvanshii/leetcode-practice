# LeetCode 2615. Sum of Distances — Medium
# https://leetcode.com/problems/sum-of-distances/
# Submission 2205103389 — Accepted, Python3
#
# My thinking: equal values only interact with each other, so
# group indices by value. Inside a group, prefix sums give
# each index its total distance to the left and to the right
# in O(1).
from collections import defaultdict


class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        groups = defaultdict(list)
        for i, x in enumerate(nums):
            groups[x].append(i)
        ans = [0] * len(nums)
        for idxs in groups.values():
            pref = [0]
            for i in idxs:
                pref.append(pref[-1] + i)
            m = len(idxs)
            for p, i in enumerate(idxs):
                ans[i] = (i * p - pref[p]
                          + (pref[m] - pref[p + 1]) - i * (m - p - 1))
        return ans
