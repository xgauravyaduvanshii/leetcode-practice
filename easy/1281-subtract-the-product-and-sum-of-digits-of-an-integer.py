# LeetCode 1281. Subtract the Product and Sum of Digits of an Integer — Easy
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# Submission 2197566924 — Accepted, Python3
#
# My thinking: I peel the digits off one by one from
# the right, multiplying them together and adding
# them up at the same time. The answer is just the
# product minus the sum.

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        while n > 0:
            digit = n % 10
            product *= digit
            total += digit
            n //= 10
        return product - total
