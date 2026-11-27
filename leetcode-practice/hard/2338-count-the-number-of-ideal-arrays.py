# LeetCode 2338. Count the Number of Ideal Arrays — Hard
# https://leetcode.com/problems/count-the-number-of-ideal-arrays/
# Submission 2201687691 — Accepted, Python3
#
# My thinking: an ideal array is a chain
# of divisors stretched over the slots — I
# count how many chains of each length
# exist, then choose where each new value
# first appears.

MOD = 10 ** 9 + 7


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        dp = [1] * (maxValue + 1)
        chains = [0]
        chains.append(maxValue)
        length = 2
        while True:
            ndp = [0] * (maxValue + 1)
            for u in range(1, maxValue + 1):
                if dp[u] == 0:
                    continue
                m = u * 2
                while m <= maxValue:
                    ndp[m] = (ndp[m] + dp[u]) % MOD
                    m += u
            total = sum(ndp) % MOD
            if total == 0:
                break
            chains.append(total)
            dp = ndp
            length += 1
        ans = 0
        for k in range(1, len(chains)):
            ans = (ans + chains[k] * comb(n - 1, k - 1)) % MOD
        return ans
