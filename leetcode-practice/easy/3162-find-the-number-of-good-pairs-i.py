# 3162. Find the Number of Good Pairs I (Easy)
# https://leetcode.com/problems/find-the-number-of-good-pairs-i/
# Submission 2199982976 — Accepted, Python3
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # My thinking: a pair is good when the first
        # number divides evenly by the second number
        # times k. I just try every pair and count the
        # ones that divide cleanly.
        count = 0
        for a in nums1:
            for b in nums2:
                if a % (b * k) == 0:
                    count += 1
        return count
