# LeetCode 318. Maximum Product of Word Lengths — Medium
# https://leetcode.com/problems/maximum-product-of-word-lengths/
# Submission 2198744498 — Accepted, Python3
#
# My thinking: two words share no letter exactly
# when their letter bitmasks do not overlap. I turn
# each word into a 26-bit mask, then check every
# pair with one AND and keep the biggest product of
# lengths.

from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = []
        for word in words:
            mask = 0
            for char in set(word):
                mask |= 1 << (ord(char) - ord("a"))
            masks.append(mask)
        best = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if masks[i] & masks[j] == 0:
                    best = max(best, len(words[i]) * len(words[j]))
        return best
