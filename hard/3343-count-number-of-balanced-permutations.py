# LeetCode 3343. Count Number of Balanced Permutations — Hard
# https://leetcode.com/problems/count-number-of-balanced-permutations/
# Submission 2202393252 — Accepted, Python3
MOD = 10 ** 9 + 7


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        # My thinking: the digit sum must be even, with half of it on the
        # even positions. I choose which copies of each digit go to the even
        # slots with a DP over digits, tracking how many even slots are
        # filled and their digit sum. To count distinct permutations I weight
        # each choice by 1/k! * 1/(cnt-k)! (the multinomial denominators),
        # then multiply by even! * odd! at the end, which restores the exact
        # count of distinct arrangements of both halves.
        digits = [int(c) for c in num]
        total = sum(digits)
        if total % 2:
            return 0
        n = len(digits)
        n_even = (n + 1) // 2
        n_odd = n // 2
        target = total // 2
        cnt = [0] * 10
        for d in digits:
            cnt[d] += 1
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD
        dp = [[0] * (target + 1) for _ in range(n_even + 1)]
        dp[0][0] = 1
        for d in range(10):
            c = cnt[d]
            if c == 0:
                continue
            ndp = [[0] * (target + 1) for _ in range(n_even + 1)]
            for e in range(n_even + 1):
                for s in range(target + 1):
                    v = dp[e][s]
                    if not v:
                        continue
                    for k in range(0, min(c, n_even - e) + 1):
                        ns = s + k * d
                        if ns > target:
                            break
                        ndp[e + k][ns] = (ndp[e + k][ns]
                                          + v * inv_fact[k] % MOD
                                          * inv_fact[c - k]) % MOD
            dp = ndp
        return dp[n_even][target] * fact[n_even] % MOD * fact[n_odd] % MOD
