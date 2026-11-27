# LeetCode 2806. Account Balance After Rounded Purchase — Easy
# https://leetcode.com/problems/account-balance-after-rounded-purchase/
# Submission 2198414121 — Accepted, Python3
#
# My thinking: the price is rounded to the nearest
# multiple of 10, with a 5 rounding up — adding 5
# before dropping the last digit does exactly that.
# The balance is 100 minus the rounded price.

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rounded = ((purchaseAmount + 5) // 10) * 10
        return 100 - rounded
