# LeetCode 2169. Count Operations to Obtain Zero — Easy
# https://leetcode.com/problems/count-operations-to-obtain-zero/
# Submission 2197616184 — Accepted, Python3
#
# My thinking: each operation subtracts the smaller
# number from the bigger one. Instead of subtracting
# one at a time, I count how many whole times the
# smaller number fits into the bigger one and take
# the remainder in one step — like the Euclidean
# algorithm.

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ops = 0
        while num1 and num2:
            if num1 >= num2:
                ops += num1 // num2
                num1 %= num2
            else:
                ops += num2 // num1
                num2 %= num1
        return ops
