# LeetCode 916. Word Subsets — Medium
# https://leetcode.com/problems/word-subsets/
# Submission 2198969087 — Accepted, Python3
#
# My thinking: every word in the second list
# sets a minimum count for each letter. I merge
# those into one requirement, then keep the
# first-list words that cover every letter in
# it.

from collections import Counter
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        needed = Counter()
        for word in words2:
            counts = Counter(word)
            for letter, count in counts.items():
                needed[letter] = max(needed[letter], count)
        result = []
        for word in words1:
            counts = Counter(word)
            if all(counts[letter] >= count for letter, count in needed.items()):
                result.append(word)
        return result
