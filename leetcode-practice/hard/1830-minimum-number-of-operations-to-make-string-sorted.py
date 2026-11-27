# LeetCode 1830. Minimum Number of Operations to Make String Sorted — Hard
# https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/
# Submission 2201190740 — Accepted, Python3
#
# My thinking: the answer is how many distinct
# arrangements of the same letters come before
# this string — at each position I try every
# smaller letter still unused and count the
# arrangements of what is left.

from collections import Counter

MOD = 10 ** 9 + 7

class Solution:
    def makeStringSorted(self, s: str) -> int:
        n = len(s)
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD
        cnt = Counter(s)
        ans = 0
        for i, ch in enumerate(s):
            for c in range(ord(ch) - 97):
                letter = chr(c + 97)
                if cnt[letter] == 0:
                    continue
                denom = 1
                for k, v in cnt.items():
                    denom = denom * (inv_fact[v - 1] if k == letter else inv_fact[v]) % MOD
                ans = (ans + fact[n - 1 - i] * denom) % MOD
            cnt[ch] -= 1
        return ans
