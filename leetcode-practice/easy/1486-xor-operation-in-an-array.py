# LeetCode 1486. XOR Operation in an Array — Easy
# https://leetcode.com/problems/xor-operation-in-an-array/
# Submission 2197581886 — Accepted, Python3
#
# My thinking: the array is just start, start+2,
# start+4, and so on for n numbers. I build each
# one and xor them all together.

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            result ^= start + 2 * i
        return result
