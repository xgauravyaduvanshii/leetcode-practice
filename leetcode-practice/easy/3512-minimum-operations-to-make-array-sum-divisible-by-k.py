# 3512. Minimum Operations to Make Array Sum Divisible by K (Easy)
# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/
# Submission 2200025906 — Accepted, Python3
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # My thinking: each operation drops one element
        # by one, so the sum drops by one too. To make
        # the sum divisible by k I need to shave off
        # exactly the remainder of the sum divided by
        # k.
        return sum(nums) % k
