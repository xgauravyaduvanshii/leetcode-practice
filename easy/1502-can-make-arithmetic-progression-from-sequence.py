# LeetCode 1502. Can Make Arithmetic Progression From Sequence — Easy
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
# Submission 2197582682 — Accepted, Python3
#
# My thinking: I sort the numbers, then the gap
# between the first two fixes the step size. If
# every following gap is the same, the sequence
# can be an arithmetic progression.

class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True
