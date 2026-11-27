# LeetCode 2614. Prime In Diagonal — Easy
# https://leetcode.com/problems/prime-in-diagonal/
# Submission 2197811014 — Accepted, Python3
#
# My thinking: only the two diagonals matter — the
# main diagonal and the anti-diagonal. I check each
# number on them for primality and keep the biggest
# prime I find.

from typing import List


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(x):
            if x < 2:
                return False
            d = 2
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 1
            return True
        n = len(nums)
        best = 0
        for i in range(n):
            for x in (nums[i][i], nums[i][n - 1 - i]):
                if x > best and is_prime(x):
                    best = x
        return best
