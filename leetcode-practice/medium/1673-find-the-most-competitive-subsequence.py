# LeetCode 1673. Find the Most Competitive Subsequence — Medium
# https://leetcode.com/problems/find-the-most-competitive-subsequence/
# Submission 2199907220 — Accepted, Python3
#
# My thinking: I build the answer greedily —
# a bigger earlier value is only worth keeping
# if I cannot afford to drop it. A monotone
# stack drops it exactly when I can.

from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        drop = len(nums) - k
        for num in nums:
            while stack and stack[-1] > num and drop > 0:
                stack.pop()
                drop -= 1
            stack.append(num)
        return stack[:k]
