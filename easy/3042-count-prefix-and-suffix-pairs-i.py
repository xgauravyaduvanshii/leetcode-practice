# 3042. Count Prefix and Suffix Pairs I (Easy)
# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/
# Submission 2199970534 — Accepted, Python3
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # My thinking: check every pair in order. The
        # earlier word counts when it starts the later
        # word and also ends it — both must hold.
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1
        return count
