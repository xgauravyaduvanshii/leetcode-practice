# 3838. Weighted Word Mapping (Easy)
# https://leetcode.com/problems/weighted-word-mapping/
# Submission 2200071609 — Accepted, Python3
from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # My thinking: add up each word's letter
        # weights, take the remainder after dividing
        # by 26, and read it off the alphabet
        # backwards — 0 is z, 1 is y, all the way to
        # 25 is a.
        out = []
        for word in words:
            total = sum(weights[ord(ch) - ord("a")] for ch in word)
            out.append(chr(ord("z") - total % 26))
        return "".join(out)
