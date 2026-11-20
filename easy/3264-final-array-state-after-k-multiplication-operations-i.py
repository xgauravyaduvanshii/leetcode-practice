# 3264. Final Array State After K Multiplication Operations I (Easy)
# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/
# Submission 2199990818 — Accepted, Python3
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # My thinking: repeat k times — find the
        # smallest number (the first one if there is a
        # tie) and multiply it. After k rounds the list
        # is the answer.
        for _ in range(k):
            i = nums.index(min(nums))
            nums[i] *= multiplier
        return nums
