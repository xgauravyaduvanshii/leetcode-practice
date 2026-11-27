# LeetCode 268. Missing Number — Easy
# https://leetcode.com/problems/missing-number/
# Submission 2197460968 — Accepted, Python3
#
# My thinking: the numbers are supposed to be 0 to n,
# so their sum should be n * (n + 1) / 2. Whatever is
# missing from that total is the number that is not
# in the list.

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
