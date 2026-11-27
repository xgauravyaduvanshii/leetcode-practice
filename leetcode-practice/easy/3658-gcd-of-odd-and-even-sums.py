# 3658. GCD of Odd and Even Sums (Easy)
# https://leetcode.com/problems/gcd-of-odd-and-even-sums/
# Submission 2200035074 — Accepted, Python3
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # My thinking: the first n odd numbers add up
        # to n squared, and the first n even numbers add
        # up to n times n plus one. Those two share
        # exactly n as their greatest common divisor.
        return n
