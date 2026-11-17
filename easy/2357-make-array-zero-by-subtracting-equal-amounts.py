# LeetCode 2357. Make Array Zero by Subtracting Equal Amounts — Easy
# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
# Submission 2197774190 — Accepted, Python3
#
# My thinking: each operation can subtract the same
# amount from all remaining positive numbers. So the
# number of operations is just the count of distinct
# positive values — each distinct value needs one
# operation to reach zero.

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return len(set(x for x in nums if x > 0))
