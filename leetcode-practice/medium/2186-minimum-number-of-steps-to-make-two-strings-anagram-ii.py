# LeetCode 2186. Minimum Number of Steps to Make Two Strings Anagram II — Medium
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/
# Submission 2204491299 — Accepted, Python3
#
# My thinking: two strings are anagrams when every letter appears the
# same number of times in both. Each step changes one letter in one
# string, fixing one unit of difference, so the answer is the total
# absolute difference of the letter counts across all letters.
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        cs = Counter(s)
        ct = Counter(t)
        return sum(abs(cs[ch] - ct[ch]) for ch in set(cs) | set(ct))
