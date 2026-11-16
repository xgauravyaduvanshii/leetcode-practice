# LeetCode 1304. Find N Unique Integers Sum up to Zero — Easy
# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# Submission 2197568679 — Accepted, Python3
#
# My thinking: pairs of opposites cancel out, so I
# just take 1 and -1, 2 and -2, and so on. If n is
# odd, I add a 0 at the end — it is unique and
# does not change the sum.

class Solution:
    def sumZero(self, n: int) -> list[int]:
        result = []
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
        if n % 2 == 1:
            result.append(0)
        return result
