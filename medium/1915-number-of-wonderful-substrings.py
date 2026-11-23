# LeetCode 1915. Number of Wonderful Substrings — Medium
# https://leetcode.com/problems/number-of-wonderful-substrings/
# Submission 2201589941 — Accepted, Python3
#
# My thinking: a substring is wonderful when
# at most one letter shows up an odd number of
# times, so I only track the odd-or-even of
# each letter as I walk — two prefixes match
# when their odd-sets are equal or differ by
# a single letter.

from collections import Counter


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        counts = Counter({0: 1})
        mask = 0
        ans = 0
        for ch in word:
            mask ^= 1 << (ord(ch) - ord('a'))
            ans += counts[mask]
            for b in range(10):
                ans += counts[mask ^ (1 << b)]
            counts[mask] += 1
        return ans
