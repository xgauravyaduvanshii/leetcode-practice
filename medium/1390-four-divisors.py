# LeetCode 1390. Four Divisors — Medium
# https://leetcode.com/problems/four-divisors/
# Submission 2199047608 — Accepted, Python3
#
# My thinking: a number has exactly four
# divisors when it has exactly two divisor
# pairs besides one and itself. I find those
# pairs by checking up to the square root and
# add up the qualifying numbers.

from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            divisors = []
            for d in range(2, int(num ** 0.5) + 1):
                if num % d == 0:
                    divisors.append(d)
                    if d * d != num:
                        divisors.append(num // d)
            if len(divisors) == 2:
                total += 1 + num + sum(divisors)
        return total
