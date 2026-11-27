# LeetCode 2303. Calculate Amount Paid in Taxes — Easy
# https://leetcode.com/problems/calculate-amount-paid-in-taxes/
# Submission 2197622489 — Accepted, Python3
#
# My thinking: I walk through the tax brackets in
# order. For each bracket I tax only the part of
# the income that falls inside it, and stop once
# the income runs out.

class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        tax = 0.0
        prev = 0
        for upper, percent in brackets:
            taxable = min(income, upper) - prev
            if taxable <= 0:
                break
            tax += taxable * percent / 100
            prev = upper
        return tax
