# LeetCode 560. Subarray Sum Equals K — Medium
# https://leetcode.com/problems/subarray-sum-equals-k/
# Submission 2198864618 — Accepted, Python3
#
# My thinking: a subarray sums to k when two running
# totals differ by exactly k. I count how often
# each total has appeared and add up the matches as
# I walk along.

from collections import Counter
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = Counter([0])
        running = 0
        total = 0
        for num in nums:
            running += num
            total += counts[running - k]
            counts[running] += 1
        return total
