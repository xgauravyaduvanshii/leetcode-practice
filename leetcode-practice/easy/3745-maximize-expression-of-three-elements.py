# 3745. Maximize Expression of Three Elements (Easy)
# https://leetcode.com/problems/maximize-expression-of-three-elements/
# Submission 2200059122 — Accepted, Python3
from typing import List


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        # My thinking: to make a plus b minus c as big
        # as possible, take the two biggest numbers for
        # a and b, and the smallest number for c.
        nums = sorted(nums)
        return nums[-1] + nums[-2] - nums[0]
