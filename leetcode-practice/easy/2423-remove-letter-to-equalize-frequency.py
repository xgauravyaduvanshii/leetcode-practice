# LeetCode 2423. Remove Letter To Equalize Frequency — Easy
# https://leetcode.com/problems/remove-letter-to-equalize-frequency/
# Submission 2197781859 — Accepted, Python3
#
# My thinking: I try removing one occurrence of each
# distinct letter in turn. If after a removal every
# remaining letter has the same frequency, the word
# can be equalized.

from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        counts = Counter(word)
        for ch in list(counts):
            counts[ch] -= 1
            if counts[ch] == 0:
                del counts[ch]
            if len(set(counts.values())) == 1:
                return True
            counts[ch] = counts.get(ch, 0) + 1
        return False
