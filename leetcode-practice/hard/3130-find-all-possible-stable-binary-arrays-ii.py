# LeetCode 3130. Find All Possible Stable Binary Arrays II — Hard
# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/
# Submission 2202019719 — Accepted, Python3
#
# My thinking: I count arrays ending in
# 0 and ending in 1 separately, tracking
# how many of each symbol were used. An
# array ending in 0 extends any array
# ending in 1, plus runs of zeros up to
# the limit — I keep those sums in a
# sliding window, and the same the other
# way round for arrays ending in 1.

from typing import List


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 1000000007
        A_all = []
        B_all = []
        colB = [0] * (one + 1)
        for z in range(zero + 1):
            Arow = [0] * (one + 1)
            Brow = [0] * (one + 1)
            prevB = B_all[z - 1] if z >= 1 else None
            dropB = B_all[z - limit - 1] if z - limit - 1 >= 0 else None
            rowSum = 0
            for o in range(one + 1):
                if prevB is not None:
                    colB[o] += prevB[o]
                    if dropB is not None:
                        colB[o] -= dropB[o]
                if z > 0:
                    if o == 0:
                        Arow[o] = 1 if z <= limit else 0
                    else:
                        Arow[o] = colB[o] % MOD
                if o >= 1:
                    rowSum += Arow[o - 1]
                    if o - limit - 1 >= 0:
                        rowSum -= Arow[o - limit - 1]
                if o > 0:
                    if z == 0:
                        Brow[o] = 1 if o <= limit else 0
                    else:
                        Brow[o] = rowSum % MOD
            A_all.append(Arow)
            B_all.append(Brow)
        return (A_all[zero][one] + B_all[zero][one]) % MOD
