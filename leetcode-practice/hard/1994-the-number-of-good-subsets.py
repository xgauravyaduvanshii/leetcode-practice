# LeetCode 1994. The Number of Good Subsets — Hard
# https://leetcode.com/problems/the-number-of-good-subsets/
# Submission 2201294230 — Accepted, Python3
#
# My thinking: a good subset's product has no
# repeated prime, so I track which primes are
# already used in a mask — square numbers are
# out at once, and the 1s just double the count.

from collections import Counter

class Solution:
    def numberOfGoodSubsets(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        def mask_of(v):
            m = 0
            for i, p in enumerate(primes):
                cnt = 0
                while v % p == 0:
                    v //= p
                    cnt += 1
                if cnt > 1:
                    return -1
                if cnt == 1:
                    m |= 1 << i
            if v > 1:
                return -1
            return m

        freq = Counter(nums)
        ones = freq.get(1, 0)
        dp = [0] * (1 << 10)
        dp[0] = 1
        for v, c in freq.items():
            if v == 1:
                continue
            m = mask_of(v)
            if m == -1:
                continue
            ndp = dp[:]
            for mask in range(1 << 10):
                if dp[mask] and (mask & m) == 0:
                    ndp[mask | m] = (ndp[mask | m] + dp[mask] * c) % MOD
            dp = ndp
        total = (sum(dp) - 1) % MOD
        return total * pow(2, ones, MOD) % MOD
