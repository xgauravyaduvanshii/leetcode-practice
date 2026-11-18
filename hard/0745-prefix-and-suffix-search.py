# LeetCode 745. Prefix and Suffix Search — Hard
# https://leetcode.com/problems/prefix-and-suffix-search/
# Submission 2198671069 — Accepted, Python3
#
# My thinking: the word list is small, so I precompute
# every prefix-plus-suffix pair once and remember the
# biggest word index that has it. Later words overwrite
# earlier ones, which is exactly the "largest index"
# the query wants.

from typing import List


class WordFilter:
    def __init__(self, words: List[str]):
        self.lookup = {}
        for index, word in enumerate(words):
            for p in range(len(word) + 1):
                for s in range(len(word) + 1):
                    key = word[:p] + "#" + word[len(word) - s:]
                    self.lookup[key] = index

    def f(self, pref: str, suff: str) -> int:
        return self.lookup.get(pref + "#" + suff, -1)
