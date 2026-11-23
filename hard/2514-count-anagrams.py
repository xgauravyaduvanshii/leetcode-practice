# LeetCode 2514. Count Anagrams — Hard
# https://leetcode.com/problems/count-anagrams/
# Submission 2201792148 — Accepted, Python3
#
# My thinking: each word stands on its
# own — its distinct shuffles are its
# length factorial divided by the
# factorial of every repeated letter —
# and the words multiply together.

from collections import Counter
from math import factorial


class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        ans = 1
        for word in s.split(" "):
            ways = factorial(len(word))
            for c in Counter(word).values():
                ways //= factorial(c)
            ans = ans * ways % MOD
        return ans
