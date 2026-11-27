# 3541. Find Most Frequent Vowel and Consonant (Easy)
# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
# Submission 2200026860 — Accepted, Python3
from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        # My thinking: count every letter, then take
        # the most common vowel and the most common
        # consonant and add their counts together.
        counts = Counter(s)
        vowels = "aeiou"
        best_vowel = max((counts[v] for v in vowels), default=0)
        best_consonant = max(
            (c for ch, c in counts.items() if ch not in vowels), default=0
        )
        return best_vowel + best_consonant
