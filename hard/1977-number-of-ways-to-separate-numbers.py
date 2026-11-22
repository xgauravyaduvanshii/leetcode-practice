# LeetCode 1977. Number of Ways to Separate Numbers — Hard
# https://leetcode.com/problems/number-of-ways-to-separate-numbers/
# Submission 2201284181 — Accepted, Python3
#
# My thinking: the numbers are all positive, so
# no number may start with 0 — not even a lone
# 0. Two numbers compare by length first, then
# by their first differing digit, so I precompute
# longest common prefixes and count the splits
# with a prefix-summed table.

class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(num)
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if num[i] == num[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1

        def le(a, b, length):
            common = lcp[a][b]
            if common >= length:
                return True
            return num[a + common] < num[b + common]

        if num[0] == '0':
            return 0
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        pre = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, i):
                if num[j] == '0':
                    continue
                lo = 2 * j - i + 1
                if lo < 0:
                    lo = 0
                total = 0
                if lo <= j - 1:
                    total = (pre[j][j - 1] - (pre[j][lo - 1] if lo > 0 else 0)) % MOD
                k0 = 2 * j - i
                if 0 <= k0 < j and le(k0, j, j - k0):
                    total = (total + dp[j][k0]) % MOD
                dp[i][j] = total
            s = 0
            for k in range(i):
                s = (s + dp[i][k]) % MOD
                pre[i][k] = s
        return sum(dp[n][j] for j in range(n)) % MOD
