# LeetCode 2535. Difference Between Element Sum and Digit Sum of an Array — Easy
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
# Submission 2197799725 — Accepted, Python3
#
# My thinking: I add up all the numbers, and
# separately add up every digit of every number.
# The answer is the absolute difference of the two
# sums.

class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum = sum(nums)
        digit_sum = sum(int(ch) for x in nums for ch in str(x))
        return abs(element_sum - digit_sum)
