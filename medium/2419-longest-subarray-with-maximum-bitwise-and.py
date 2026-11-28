# LeetCode 2419. Longest Subarray With Maximum Bitwise AND — Medium
# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/
# Submission 2204859439 — Accepted, Python3
#
# My thinking: the AND of a subarray can never exceed the largest
# element in it, and a single element achieves its own value — so the
# maximum possible AND is max(nums), and the answer is simply the
# longest run of that maximum value.
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)
        best = cur = 0
        for x in nums:
            cur = cur + 1 if x == target else 0
            best = max(best, cur)
        return best
