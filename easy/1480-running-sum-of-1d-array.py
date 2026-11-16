# LeetCode 1480. Running Sum of 1d Array — Easy
# https://leetcode.com/problems/running-sum-of-1d-array/
# Submission 2197285683 — Accepted, Python3
#
# My thinking: keep a running total as I walk through
# the array, and write down the total after each
# number. That list is the running sum.

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        answer = []
        total = 0
        for num in nums:
            total += num
            answer.append(total)
        return answer
