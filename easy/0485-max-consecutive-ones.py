# LeetCode 485. Max Consecutive Ones — Easy
# https://leetcode.com/problems/max-consecutive-ones/
# Submission 2197483311 — Accepted, Python3
#
# My thinking: I walk through the numbers keeping a
# running count of the current run of 1s. A 0 resets
# it. The best run I have seen so far is the answer.

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        best = current = 0
        for num in nums:
            if num == 1:
                current += 1
                best = max(best, current)
            else:
                current = 0
        return best
