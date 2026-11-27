# 3982. Sum of Integers With Maximum Digit Range (Easy)
# https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/
# Submission 2200092946 — Accepted, Python3
class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        # My thinking: for each number I take its
        # biggest digit minus its smallest digit. I
        # find the largest such range, then add up
        # every number that reaches it.
        def digit_range(x: int) -> int:
            digits = [int(d) for d in str(x)]
            return max(digits) - min(digits)

        top = max(digit_range(x) for x in nums)
        return sum(x for x in nums if digit_range(x) == top)
