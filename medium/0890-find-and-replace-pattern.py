# LeetCode 890. Find and Replace Pattern — Medium
# https://leetcode.com/problems/find-and-replace-pattern/
# Submission 2198964879 — Accepted, Python3
#
# My thinking: a word matches the pattern when
# its letters map to the pattern's letters in a
# one-to-one way — the same letter always maps to
# the same letter, and two letters never share
# one. I check both directions of the mapping.

from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def matches(word):
            if len(word) != len(pattern):
                return False
            word_to_pattern = {}
            pattern_to_word = {}
            for w, p in zip(word, pattern):
                if w in word_to_pattern and word_to_pattern[w] != p:
                    return False
                if p in pattern_to_word and pattern_to_word[p] != w:
                    return False
                word_to_pattern[w] = p
                pattern_to_word[p] = w
            return True

        return [word for word in words if matches(word)]
