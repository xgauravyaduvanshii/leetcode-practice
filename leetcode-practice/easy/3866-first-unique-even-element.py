# 3866. First Unique Even Element (Easy)
# https://leetcode.com/problems/first-unique-even-element/
# Submission 2200082788 — Accepted, Python3
from collections import Counter


class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        # My thinking: count how often each number
        # appears, then take the first even number in
        # the array that shows up exactly once.
        counts = Counter(nums)
        for x in nums:
            if x % 2 == 0 and counts[x] == 1:
                return x
        return -1
