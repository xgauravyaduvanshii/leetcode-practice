# LeetCode 491. Non-decreasing Subsequences — Medium
# https://leetcode.com/problems/non-decreasing-subsequences/
# Submission 2198824251 — Accepted, Python3
#
# My thinking: I build subsequences by choosing
# later elements that do not go down. At each step
# I skip a value I already tried there, so the same
# subsequence is never built twice from equal
# numbers.

from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, current):
            if len(current) >= 2:
                result.append(list(current))
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                if not current or nums[i] >= current[-1]:
                    used.add(nums[i])
                    current.append(nums[i])
                    backtrack(i + 1, current)
                    current.pop()

        backtrack(0, [])
        return result
