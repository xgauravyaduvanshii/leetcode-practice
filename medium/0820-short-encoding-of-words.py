# LeetCode 820. Short Encoding of Words — Medium
# https://leetcode.com/problems/short-encoding-of-words/
# Submission 2198947372 — Accepted, Python3
#
# My thinking: a word that is the ending of
# another word rides along for free. I drop every
# such suffix from the set, then add up the
# remaining words plus one separator each.

from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        unique = set(words)
        for word in words:
            for i in range(1, len(word)):
                unique.discard(word[i:])
        return sum(len(word) + 1 for word in unique)
