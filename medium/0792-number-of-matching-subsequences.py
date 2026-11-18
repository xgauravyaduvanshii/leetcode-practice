# LeetCode 792. Number of Matching Subsequences — Medium
# https://leetcode.com/problems/number-of-matching-subsequences/
# Submission 2198939226 — Accepted, Python3
#
# My thinking: I group the words by the letter
# each is waiting for. Reading the string once,
# every word moves to the bucket of its next
# letter — and when a word runs out of letters it
# has matched. Each word's iterator is advanced
# past its first letter when seeded, since that
# letter is the bucket key itself.

from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = defaultdict(list)
        for word in words:
            it = iter(word)
            next(it)
            buckets[word[0]].append(it)
        matched = 0
        for ch in s:
            waiting = buckets.pop(ch, [])
            for it in waiting:
                nxt = next(it, None)
                if nxt is None:
                    matched += 1
                else:
                    buckets[nxt].append(it)
        return matched
