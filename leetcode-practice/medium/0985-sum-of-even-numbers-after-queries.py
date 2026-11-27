# LeetCode 985. Sum of Even Numbers After Queries — Medium
# https://leetcode.com/problems/sum-of-even-numbers-after-queries/
# Submission 2197547915 — Accepted, Python3
#
# My thinking: instead of re-adding all the even
# numbers after every query, I keep a running
# total. When a query changes a number, I subtract
# it from the total first if it was even, apply the
# change, then add it back if it is even now.

class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        total = sum(x for x in nums if x % 2 == 0)
        result = []
        for val, index in queries:
            if nums[index] % 2 == 0:
                total -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                total += nums[index]
            result.append(total)
        return result
