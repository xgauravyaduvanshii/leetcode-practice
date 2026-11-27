# LeetCode 3045. Count Prefix and Suffix Pairs II — Hard
# https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/
# Submission 2201909099 — Accepted, Python3
#
# My thinking: a word only pairs with an
# earlier word that is one of its borders
# — a proper head that is also its tail
# — or the word itself. I walk each
# word's borders through its KMP prefix
# links and count how many earlier words
# match each border. Borders are keyed
# by length and a double rolling hash, so
# looking one up never copies the string.

from typing import List

MOD1 = 1_000_000_007
MOD2 = 1_000_000_009
BASE = 127


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        max_len = max((len(w) for w in words), default=0)
        pow1 = [1] * (max_len + 1)
        pow2 = [1] * (max_len + 1)
        for i in range(1, max_len + 1):
            pow1[i] = pow1[i - 1] * BASE % MOD1
            pow2[i] = pow2[i - 1] * BASE % MOD2

        def prefix_hashes(w: str):
            h1 = [0] * (len(w) + 1)
            h2 = [0] * (len(w) + 1)
            for i, ch in enumerate(w):
                v = ord(ch)
                h1[i + 1] = (h1[i] * BASE + v) % MOD1
                h2[i + 1] = (h2[i] * BASE + v) % MOD2
            return h1, h2

        def pi_array(w: str):
            n = len(w)
            pi = [0] * n
            for i in range(1, n):
                j = pi[i - 1]
                while j > 0 and w[i] != w[j]:
                    j = pi[j - 1]
                if w[i] == w[j]:
                    j += 1
                pi[i] = j
            return pi

        seen = {}
        ans = 0
        for w in words:
            h1, h2 = prefix_hashes(w)
            pi = pi_array(w)
            # Every border length, from the whole word down
            # through the KMP links.
            length = len(w)
            while length > 0:
                key = (length, h1[length], h2[length])
                ans += seen.get(key, 0)
                length = pi[length - 1]
            key = (len(w), h1[len(w)], h2[len(w)])
            seen[key] = seen.get(key, 0) + 1
        return ans
