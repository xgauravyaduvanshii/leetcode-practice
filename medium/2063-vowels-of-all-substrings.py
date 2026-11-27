# LeetCode 2063. Vowels of All Substrings — Medium
# https://leetcode.com/problems/vowels-of-all-substrings/
# Submission 2204392111 — Accepted, Python3
#
# My thinking: a vowel at position i appears in every substring that
# starts at or before i and ends at or after i — that is (i + 1)
# choices for the start times (n - i) choices for the end. Summing
# that product over all vowel positions counts every vowel occurrence
# in every substring exactly once.
class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        return sum((i + 1) * (n - i) for i, ch in enumerate(word) if ch in 'aeiou')
