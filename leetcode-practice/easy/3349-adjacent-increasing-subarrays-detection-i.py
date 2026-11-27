# 3349. Adjacent Increasing Subarrays Detection I (Easy)
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/
# Submission 2200007115 — Accepted, Python3
from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # My thinking: a subarray is increasing when
        # every step goes up. I look at every pair of
        # neighbours — one ending just before the other
        # starts — and check whether both runs of length
        # k climb the whole way.
        n = len(nums)
        for a in range(n - 2 * k + 1):
            first = all(nums[a + i] < nums[a + i + 1] for i in range(k - 1))
            second = all(nums[a + k + i] < nums[a + k + i + 1] for i in range(k - 1))
            if first and second:
                return True
        return False
