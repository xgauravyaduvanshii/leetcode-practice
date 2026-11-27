# LeetCode 3700. Number of ZigZag Arrays II — Hard
# https://leetcode.com/problems/number-of-zigzag-arrays-ii/
# Submission 2203051660 — Accepted, Python3
from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        # My thinking: only the relative order of values matters,
        # so relabel them 0..m-1. Track, for arrays built so far,
        # U[v] = count ending in v with the last step up and
        # D[v] = count ending in v with the last step down. One
        # more step is a prefix sum of D for the new U and a
        # suffix sum of U for the new D, because an up step is
        # only allowed after a down step (and vice versa) — that
        # is exactly what forbids three in a row going the same
        # way. Two steps therefore decouple: U evolves by
        # A = L*R with A[i][j] = min(i, j), D by its mirror
        # image, so I raise A to the needed power with binary
        # exponentiation and finish with at most one extra step.
        m = r - l + 1
        # Length-2 arrays: U[v] counts smaller first values, D[v]
        # counts larger first values.
        u0 = list(range(m))
        d0 = [m - 1 - i for i in range(m)]
        if n == 2:
            return (sum(u0) + sum(d0)) % MOD
        k, odd = divmod(n - 2, 2)
        # A[i][j] = min(i, j).
        A = [[min(i, j) for j in range(m)] for i in range(m)]
        P = self._mat_pow(A, k)
        # W[i] = sum_j P[i][j] * j. U after 2k steps is W, and D
        # after 2k steps is W reversed (mirror symmetry: the
        # down-counts from the top behave like up-counts from
        # the bottom).
        W = [sum(P[i][j] * j for j in range(m)) % MOD for i in range(m)]
        U = W
        D = W[::-1]
        if odd == 0:
            return (sum(U) + sum(D)) % MOD
        # One more step: new U is prefix sums of D, new D is
        # suffix sums of U.
        new_u = 0
        run = 0
        for v in D:
            new_u = (new_u + run) % MOD
            run = (run + v) % MOD
        new_d = 0
        run = 0
        for v in reversed(U):
            new_d = (new_d + run) % MOD
            run = (run + v) % MOD
        return (new_u + new_d) % MOD

    def _mat_mul(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        n = len(A)
        C = [[0] * n for _ in range(n)]
        for i in range(n):
            Ci = C[i]
            Ai = A[i]
            for kk in range(n):
                aik = Ai[kk]
                if aik:
                    Bk = B[kk]
                    for j in range(n):
                        Ci[j] += aik * Bk[j]
            for j in range(n):
                Ci[j] %= MOD
        return C

    def _mat_pow(self, A: List[List[int]], e: int) -> List[List[int]]:
        n = len(A)
        res = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        base = A
        while e:
            if e & 1:
                res = self._mat_mul(res, base)
            base = self._mat_mul(base, base)
            e >>= 1
        return res
