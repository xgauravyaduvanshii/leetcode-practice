# 3487. Maximum Unique Subarray Sum After Deletion (Easy)
# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/
# Submission 2200021396 — Accepted, Python3
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # My thinking: I can delete anything, so I keep
        # one copy of every positive number and drop
        # the rest — negatives and duplicates only drag
        # the sum down. If there is no positive number
        # at all, the best I can do is the largest one.
        positives = {n for n in nums if n > 0}
        if positives:
            return sum(positives)
        return max(nums)
