# LeetCode 2588. Count the Number of Beautiful Subarrays — Medium
# https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/
# Submission 2205088593 — Accepted, Python3
#
# My thinking: a subarray is beautiful exactly when every bit
# appears an even number of times, which is the same as its
# XOR being zero. Equal prefix XORs mark exactly those
# subarrays, so count pairs of equal prefix XORs.
from collections import defaultdict


class Solution:
    def beautifulSubarrays(self, nums: list[int]) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        pref = 0
        ans = 0
        for x in nums:
            pref ^= x
            ans += freq[pref]
            freq[pref] += 1
        return ans
