# LeetCode 2572. Count the Number of Square-Free Subsets — Medium
# https://leetcode.com/problems/count-the-number-of-square-free-subsets/
# Submission 2205074924 — Accepted, Python3
#
# My thinking: a product is square-free exactly when no prime
# appears twice, so each number becomes a mask over the ten
# primes up to 30. Numbers divisible by a squared prime can
# never be used; 1s are free multipliers. DP over masks counts
# the valid subsets of non-1 numbers, and the all-1s subsets
# are added separately (the formula must not drop them).
class Solution:
    def squareFreeSubsets(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        pidx = {p: i for i, p in enumerate(primes)}
        ones = 0
        dp = [0] * 1024
        dp[0] = 1
        for x in nums:
            if x == 1:
                ones += 1
                continue
            mask = 0
            ok = True
            y = x
            for p in primes:
                if p * p > y:
                    break
                if y % p == 0:
                    if y % (p * p) == 0:
                        ok = False
                        break
                    mask |= 1 << pidx[p]
                    y //= p
            if not ok:
                continue
            if y > 1:
                mask |= 1 << pidx[y]
            ndp = dp[:]
            for m in range(1024):
                if m & mask == 0:
                    ndp[m | mask] = (ndp[m | mask] + dp[m]) % MOD
            dp = ndp
        pow_ones = pow(2, ones, MOD)
        total = (sum(dp) - 1) * pow_ones + (pow_ones - 1)
        return total % MOD
