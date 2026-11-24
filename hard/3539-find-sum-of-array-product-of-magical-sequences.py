# LeetCode 3539. Find Sum of Array Product of Magical Sequences — Hard
# https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/
# Submission 2202818897 — Accepted, Python3
from typing import List
from collections import defaultdict

MOD = 10 ** 9 + 7


class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        # My thinking: a sequence is fixed by how many times each
        # index is used, and the sum 2^seq[0] + ... is read bit by
        # bit with carries: at index j, choosing c copies contributes
        # c + carry to that bit, whose parity is a set bit and whose
        # half carries on. I walk the indices keeping (carry, set
        # bits so far, elements used) and multiply by C(remaining, c)
        # times nums[j]^c, which is exactly the multinomial weight
        # of the sequences with that count. At the end the leftover
        # carry's own set bits are added to the count.
        n = len(nums)
        C = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            C[i][0] = C[i][i] = 1
            for j in range(1, i):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD
        pw = [[1] * (m + 1) for _ in range(n)]
        for j in range(n):
            for c in range(1, m + 1):
                pw[j][c] = pw[j][c - 1] * nums[j] % MOD
        dp = {(0, 0, 0): 1}
        for j in range(n):
            ndp = defaultdict(int)
            for (carry, bits, used), val in dp.items():
                rem = m - used
                for c in range(rem + 1):
                    s = c + carry
                    ncarry = s // 2
                    nbits = bits + (s % 2)
                    if nbits > k:
                        continue
                    nused = used + c
                    factor = C[rem][c] * pw[j][c] % MOD
                    ndp[(ncarry, nbits, nused)] = (ndp[(ncarry, nbits, nused)] + val * factor) % MOD
            dp = ndp
        ans = 0
        for (carry, bits, used), val in dp.items():
            if used == m and bits + bin(carry).count("1") == k:
                ans = (ans + val) % MOD
        return ans
