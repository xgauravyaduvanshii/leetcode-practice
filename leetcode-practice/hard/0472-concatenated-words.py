# LeetCode 472. Concatenated Words — Hard
# https://leetcode.com/problems/concatenated-words/
# Submission 2198659247 — Accepted, Python3
#
# My thinking: a word counts if it can be cut into
# two or more dictionary words. I test each word with
# the word itself taken out of the dictionary first —
# otherwise every word would trivially "match" itself
# — and mark which prefixes can be built, one cut at
# a time.

from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        known = set(words)
        found = []

        def can_form(word):
            reachable = [False] * (len(word) + 1)
            reachable[0] = True
            for end in range(1, len(word) + 1):
                for start in range(end):
                    if reachable[start] and word[start:end] in known:
                        reachable[end] = True
                        break
            return reachable[len(word)]

        for word in words:
            if not word:
                continue
            known.remove(word)
            if can_form(word):
                found.append(word)
            known.add(word)
        return found
