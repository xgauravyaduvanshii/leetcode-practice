# LeetCode 1672. Richest Customer Wealth — Easy
# https://leetcode.com/problems/richest-customer-wealth/
# Submission 2197285992 — Accepted, Python3
#
# My thinking: each customer's wealth is just the sum
# of their bank accounts. I add up every row and keep
# the biggest total I have seen.

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest = 0
        for customer in accounts:
            wealth = sum(customer)
            if wealth > richest:
                richest = wealth
        return richest
