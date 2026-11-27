# LeetCode 1160. Find Words That Can Be Formed by Characters — Easy
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
# Submission 2197559959 — Accepted, Python3
#
# My thinking: I count the letters I have available.
# A word can be formed only if I have at least as
# many of every letter it needs. I add up the
# lengths of all the words that pass that test.

from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        available = Counter(chars)
        total = 0
        for word in words:
            needed = Counter(word)
            if all(needed[ch] <= available[ch] for ch in needed):
                total += len(word)
        return total
