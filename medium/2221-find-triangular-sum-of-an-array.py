# LeetCode 2221. Find Triangular Sum of an Array — Medium
# https://leetcode.com/problems/find-triangular-sum-of-an-array/
# Submission 2204506684 — Accepted, Python3
#
# My thinking: each round replaces every adjacent pair by the sum of
# the two modulo 10, shrinking the array by one. I repeat that until a
# single number remains — that number is the triangular sum.
class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        n = len(nums)
        while n > 1:
            for i in range(n - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            n -= 1
        return nums[0]
