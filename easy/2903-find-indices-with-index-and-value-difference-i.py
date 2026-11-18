# LeetCode 2903. Find Indices With Index and Value Difference I — Easy
# https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/
# Submission 2198694761 — Accepted, Python3
#
# My thinking: the constraints are tiny, so I simply
# try every pair in order and return the first one
# whose positions are far enough apart and whose
# values differ enough. If no pair qualifies, the
# answer is -1, -1.

from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]
