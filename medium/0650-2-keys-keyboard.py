# LeetCode 650. 2 Keys Keyboard — Medium
# https://leetcode.com/problems/2-keys-keyboard/
# Submission 2198898418 — Accepted, Python3
#
# My thinking: building n letters from one is
# cheapest when the steps follow the prime factors
# of n — each factor costs exactly that many copy
# and paste operations.

class Solution:
    def minSteps(self, n: int) -> int:
        steps = 0
        factor = 2
        while n > 1:
            while n % factor == 0:
                steps += factor
                n //= factor
            factor += 1
        return steps
