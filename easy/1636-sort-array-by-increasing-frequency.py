# LeetCode 1636. Sort Array by Increasing Frequency — Easy
# https://leetcode.com/problems/sort-array-by-increasing-frequency/
# Submission 2197590925 — Accepted, Python3
#
# My thinking: I count how often each number appears,
# then sort by two rules — rarer numbers first,
# and when frequencies tie, the bigger number
# comes first.

from collections import Counter


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        counts = Counter(nums)
        return sorted(nums, key=lambda x: (counts[x], -x))
