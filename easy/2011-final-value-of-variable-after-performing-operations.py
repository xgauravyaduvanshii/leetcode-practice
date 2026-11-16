# LeetCode 2011. Final Value of Variable After Performing Operations — Easy
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
# Submission 2197609049 — Accepted, Python3
#
# My thinking: each operation either adds 1 or
# subtracts 1 from x. I just look for the '+' in
# the operation string to tell which one it is.

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0
        for op in operations:
            if '+' in op:
                x += 1
            else:
                x -= 1
        return x
