# LeetCode 2531. Make Number of Distinct Characters Equal — Medium
# https://leetcode.com/problems/make-number-of-distinct-characters-equal/
# Submission 2205052590 — Accepted, Python3
#
# My thinking: only the two distinct sets and their counts matter.
# Try every pair of characters (one from each word), simulate the
# swap on real counters, and check whether the distinct counts
# come out equal. A swap can add or remove at most one distinct
# character per word, so the simulation is exact.
from collections import Counter


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        def distinct_after(counter, out_ch, in_ch):
            if out_ch == in_ch:
                return len(counter)
            d = len(counter)
            if counter[out_ch] == 1:
                d -= 1
            if in_ch not in counter:
                d += 1
            return d

        for a in c1:
            for b in c2:
                if distinct_after(c1, a, b) == distinct_after(c2, b, a):
                    return True
        return False
