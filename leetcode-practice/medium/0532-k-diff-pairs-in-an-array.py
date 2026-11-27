# LeetCode 532. K-diff Pairs in an Array — Medium
# https://leetcode.com/problems/k-diff-pairs-in-an-array/
# Submission 2198851333 — Accepted, Python3
#
# My thinking: I count each value once, then look
# for its partner k away. When k is zero the pair
# needs the value to appear twice; otherwise each
# value with a partner counts once.

from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        pairs = 0
        for num in counts:
            if k == 0:
                if counts[num] > 1:
                    pairs += 1
            elif num + k in counts:
                pairs += 1
        return pairs
