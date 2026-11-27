# LeetCode 3292. Minimum Number of Valid Strings to Form Target II — Hard
# https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/
# Submission 2202184133 — Accepted, Python3
#
# My thinking: a valid string is any prefix of
# any word, so I hash every word prefix once.
# For each target position I binary-search the
# longest prefix that matches there (rolling
# hashes make each check O(1)), then greedily
# jump: always extend the current string as far
# as it can reach, which is optimal for the
# minimum number of strings.

from typing import List


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        mod1 = 1000000007
        mod2 = 1000000009
        base = 131
        pref_hashes = set()
        max_len = 0
        for w in words:
            max_len = max(max_len, len(w))
            h1 = 0
            h2 = 0
            for ch in w:
                v = ord(ch) - 96
                h1 = (h1 * base + v) % mod1
                h2 = (h2 * base + v) % mod2
                pref_hashes.add((h1 << 32) | h2)
        n = len(target)
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        for i in range(n):
            pow1[i + 1] = pow1[i] * base % mod1
            pow2[i + 1] = pow2[i] * base % mod2
        ph1 = [0] * (n + 1)
        ph2 = [0] * (n + 1)
        for i, ch in enumerate(target):
            v = ord(ch) - 96
            ph1[i + 1] = (ph1[i] * base + v) % mod1
            ph2[i + 1] = (ph2[i] * base + v) % mod2

        def sub_hash(i: int, length: int) -> int:
            h1 = (ph1[i + length] - ph1[i] * pow1[length]) % mod1
            h2 = (ph2[i + length] - ph2[i] * pow2[length]) % mod2
            return (h1 << 32) | h2

        def longest(i: int) -> int:
            lo = 0
            hi = min(max_len, n - i)
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if sub_hash(i, mid) in pref_hashes:
                    lo = mid
                else:
                    hi = mid - 1
            return lo

        jumps = 0
        cur_end = 0
        farthest = 0
        for i in range(n):
            if i > farthest:
                return -1
            farthest = max(farthest, i + longest(i))
            if i == cur_end:
                if farthest <= i:
                    return -1
                jumps += 1
                cur_end = farthest
                if cur_end >= n:
                    return jumps
        return -1
