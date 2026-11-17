# LeetCode 2506. Count Pairs Of Similar Strings — Easy
# https://leetcode.com/problems/count-pairs-of-similar-strings/
# Submission 2197794812 — Accepted, Python3
#
# My thinking: two words are similar when they use
# the same set of letters. I turn each word's letter
# set into a bitmask and count how many words share
# each mask — every group of c words gives c choose 2
# pairs.

from collections import Counter


class Solution:
    def similarPairs(self, words: list[str]) -> int:
        masks = Counter()
        for w in words:
            mask = 0
            for ch in set(w):
                mask |= 1 << (ord(ch) - 97)
            masks[mask] += 1
        return sum(c * (c - 1) // 2 for c in masks.values())
