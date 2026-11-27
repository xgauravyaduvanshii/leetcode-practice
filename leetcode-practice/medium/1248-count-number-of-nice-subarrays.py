# LeetCode 1248. Count Number of Nice Subarrays — Medium
# https://leetcode.com/problems/count-number-of-nice-subarrays/
# Submission 2199018062 — Accepted, Python3
#
# My thinking: I count odd numbers as I go. A
# subarray ending here is nice when the odd
# count k steps back was seen before — so I
# remember how often each odd count appeared.

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = {0: 1}
        odd = 0
        total = 0
        for value in nums:
            odd += value % 2
            total += counts.get(odd - k, 0)
            counts[odd] = counts.get(odd, 0) + 1
        return total
