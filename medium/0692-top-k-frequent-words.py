# LeetCode 692. Top K Frequent Words — Medium
# https://leetcode.com/problems/top-k-frequent-words/
# Submission 2198914849 — Accepted, Python3
#
# My thinking: I count every word, then sort by
# count descending — and alphabetically for ties —
# and take the first k.

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        return sorted(counts, key=lambda word: (-counts[word], word))[:k]
