# LeetCode 1679. Max Number of K-Sum Pairs — Medium
# https://leetcode.com/problems/max-number-of-k-sum-pairs/
# Submission 2199908045 — Accepted, Python3
#
# My thinking: every pair needs two numbers
# that add to k. I count how many of each
# value I have and match each value with its
# complement once.

from collections import Counter
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        pairs = 0
        for num in list(counts):
            need = k - num
            if need not in counts:
                continue
            if num == need:
                pairs += counts[num] // 2
            elif num < need:
                pairs += min(counts[num], counts[need])
        return pairs
