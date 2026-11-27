# LeetCode 1780. Check if Number is a Sum of Powers of Three — Medium
# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/
# Submission 2199933538 — Accepted, Python3
#
# My thinking: a sum of distinct powers of
# three is just the number written in base
# three using only zeros and ones. Any digit
# of two means it cannot be done.

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True
