# LeetCode 1952. Three Divisors — Easy
# https://leetcode.com/problems/three-divisors/
# Submission 2197605261 — Accepted, Python3
#
# My thinking: a number has exactly three divisors
# only when it is the square of a prime. So I check
# that n is a perfect square whose square root is
# prime — the root itself must have no divisor
# other than 1 and itself.

class Solution:
    def isThree(self, n: int) -> bool:
        root = int(n ** 0.5)
        if root * root != n:
            return False
        if root < 2:
            return False
        for i in range(2, int(root ** 0.5) + 1):
            if root % i == 0:
                return False
        return True
