# LeetCode 524. Longest Word in Dictionary through Deleting — Medium
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
# Submission 2198846428 — Accepted, Python3
#
# My thinking: a dictionary word works when it is a
# subsequence of the string. I test each word that
# way and keep the longest one, breaking ties by
# the smallest word.

from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word):
            i = 0
            for char in s:
                if i < len(word) and word[i] == char:
                    i += 1
            return i == len(word)

        best = ""
        for word in dictionary:
            if is_subsequence(word):
                if len(word) > len(best) or (
                    len(word) == len(best) and word < best
                ):
                    best = word
        return best
