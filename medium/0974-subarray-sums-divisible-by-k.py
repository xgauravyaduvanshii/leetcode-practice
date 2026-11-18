# LeetCode 974. Subarray Sums Divisible by K — Medium
# https://leetcode.com/problems/subarray-sums-divisible-by-k/
# Submission 2198979824 — Accepted, Python3
#
# My thinking: a subarray is divisible by k when
# the running sums at its ends leave the same
# remainder. I count how often each remainder
# has appeared, and every repeat makes a new
# valid subarray.

from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        running = 0
        total = 0
        for num in nums:
            running = (running + num) % k
            total += counts[running]
            counts[running] += 1
        return total
