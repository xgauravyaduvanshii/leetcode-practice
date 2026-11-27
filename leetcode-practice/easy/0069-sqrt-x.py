# LeetCode 69. Sqrt(x) — Easy
# https://leetcode.com/problems/sqrtx/
# Submission 2197281980 — Accepted, Python3
#
# My thinking: I cannot use pow or sqrt here, so I use
# binary search. I look for the biggest number whose
# square is still less than or equal to x — that is
# the integer square root.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer
