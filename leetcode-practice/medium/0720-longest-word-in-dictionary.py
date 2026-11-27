# LeetCode 720. Longest Word in Dictionary — Medium
# https://leetcode.com/problems/longest-word-in-dictionary/
# Submission 2198919043 — Accepted, Python3
#
# My thinking: a word counts only when the word
# without its last letter was already built. I go
# through the words shortest first, keep the ones
# that build, and remember the longest.

from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        built = {""}
        best = ""
        for word in sorted(words):
            if word[:-1] in built:
                built.add(word)
                if len(word) > len(best):
                    best = word
        return best
