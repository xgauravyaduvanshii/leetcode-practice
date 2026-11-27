# 3038. Maximum Number of Operations With the Same Score I (Easy)
# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/
# Submission 2199970284 — Accepted, Python3
from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        # My thinking: the first pair sets the score.
        # Then I keep taking pairs from the front while
        # each pair adds up to that same score — the
        # first pair that does not match ends the run.
        score = nums[0] + nums[1]
        count = 0
        i = 0
        while i + 1 < len(nums) and nums[i] + nums[i + 1] == score:
            count += 1
            i += 2
        return count
