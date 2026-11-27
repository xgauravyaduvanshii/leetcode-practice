# LeetCode 930. Binary Subarrays With Sum — Medium
# https://leetcode.com/problems/binary-subarrays-with-sum/
# Submission 2198970505 — Accepted, Python3
#
# My thinking: I count how many times each
# running sum has appeared. A subarray sums to
# the goal exactly when an earlier running sum
# was goal less than the current one.

from collections import defaultdict
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        running = 0
        total = 0
        for num in nums:
            running += num
            total += prefix_counts[running - goal]
            prefix_counts[running] += 1
        return total
