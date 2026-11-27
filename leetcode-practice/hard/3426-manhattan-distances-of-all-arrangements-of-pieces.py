# LeetCode 3426. Manhattan Distances of All Arrangements of Pieces — Hard
# https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/
# Submission 2202524642 — Accepted 919/919, Python3


class Solution:
    def manhattanDistances(self, m: int, n: int, k: int) -> int:
        # My thinking: every pair of cells shows up together in
        # exactly C(m*n - 2, k - 2) arrangements, so I only need
        # the Manhattan distance summed over all cell pairs.
        # Rows and columns split apart: the row gaps over all
        # pairs are n^2 * C(m+1, 3) and the column gaps are
        # m^2 * C(n+1, 3), then I multiply by the pair count,
        # all modulo 1e9+7.
        MOD = 10 ** 9 + 7
        total = m * n
        fact = [1] * (total + 1)
        for i in range(1, total + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (total + 1)
        inv_fact[total] = pow(fact[total], MOD - 2, MOD)
        for i in range(total, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(nn, kk):
            if kk < 0 or kk > nn:
                return 0
            return fact[nn] * inv_fact[kk] % MOD * inv_fact[nn - kk] % MOD

        # C(x+1, 3) = (x+1) * x * (x-1) / 6
        row_sum = (m + 1) * m * (m - 1) // 6
        col_sum = (n + 1) * n * (n - 1) // 6
        pair_sum = (n * n * row_sum + m * m * col_sum) % MOD
        return comb(total - 2, k - 2) * pair_sum % MOD
