# 3379. Transformed Array (Easy)
# https://leetcode.com/problems/transformed-array/
# Submission 2200009117 — Accepted, Python3
from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        # My thinking: each position looks nums[i] steps
        # away — right when it is positive, left when
        # negative — wrapping around the circle. The
        # value found there becomes the new value.
        n = len(nums)
        return [nums[(i + nums[i]) % n] for i in range(n)]
