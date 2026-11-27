# 3637. Trionic Array I (Easy)
# https://leetcode.com/problems/trionic-array-i/
# Submission 2200034425 — Accepted, Python3
from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        # My thinking: the array must climb, then fall,
        # then climb again, with each of the three
        # stretches holding at least two numbers. I
        # try every split point for the climb-fall and
        # fall-climb turns and check the three slopes.
        n = len(nums)
        for p in range(1, n - 2):
            if not all(nums[i] < nums[i + 1] for i in range(p)):
                continue
            for q in range(p + 1, n - 1):
                if not all(nums[i] > nums[i + 1] for i in range(p, q)):
                    continue
                if all(nums[i] < nums[i + 1] for i in range(q, n - 1)):
                    return True
        return False
