# LeetCode 525. Contiguous Array — Medium
# https://leetcode.com/problems/contiguous-array/
# Submission 2198847473 — Accepted, Python3
#
# My thinking: I turn 0s into -1 and track the
# running balance. Two places with the same balance
# have as many ones as zeros between them, so the
# longest such stretch is the answer.

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen = {0: -1}
        balance = 0
        best = 0
        for i, num in enumerate(nums):
            balance += 1 if num == 1 else -1
            if balance in first_seen:
                best = max(best, i - first_seen[balance])
            else:
                first_seen[balance] = i
        return best
