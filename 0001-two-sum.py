"""LeetCode 1. Two Sum — Easy
https://leetcode.com/problems/two-sum/
Submission 2197267353 — Accepted, 66/66 testcases, Python3
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
