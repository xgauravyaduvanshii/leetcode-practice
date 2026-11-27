# LeetCode 1170. Compare Strings by Frequency of the Smallest Character — Medium
# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
# Submission 2197560274 — Accepted, Python3
#
# My thinking: f(s) is how many times the smallest
# letter of s appears. I compute f for every word
# and sort those values. For each query, I need
# how many word values are bigger than its f —
# binary search on the sorted list finds where its
# f would sit, and everything after that position
# counts.

import bisect


class Solution:
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        def f(s):
            return s.count(min(s))

        word_freqs = sorted(f(w) for w in words)
        result = []
        for q in queries:
            idx = bisect.bisect_right(word_freqs, f(q))
            result.append(len(word_freqs) - idx)
        return result
